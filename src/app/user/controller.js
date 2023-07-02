import { comparePasswords, hashPassword } from "../../utils/bcrypt.js"
import { uploadProfilePic } from "../../utils/firebase.js"
import { generateJWT } from "../../utils/jwt.js"
import { checkEnigmaMembership } from "../github/repository.js"
import { createUser, getListOfMembers, getMemberProfileByUsername, getUserByEmail, getUserById, updateProfileById, userExists } from "./repository.js"
import { readFileSync, unlink } from 'fs'


/**
 * @type {import("express").RequestHandler}
 */
export const createUserController = async (req, res, next) => {
	try {
		let data = req.body
		const ghu_token = req.headers.authorization
		if(!await checkEnigmaMembership(data.profile.username, ghu_token)) {
			return res.status(403).json('User not a member of Enigma VSSUT')
		}
		if(await userExists(data.email)) {
			return res.status(400).json('User with email already exists.')
		}
		let hashedPassword = await hashPassword(data.password) 
		data.password = hashedPassword
		if(!await createUser(data)) {
			return res.status(400).json('User with username already exists.')
		}
		return res.sendStatus(201)
	}
	catch(err) {
		console.log(err)
		res.status(400).json('User with username already exists')
	}
}


/**
 * @type {import("express").RequestHandler}
 */
export const loginUserController = async (req, res, next) => {
	try {
		let { email, password } = req.body
		if(!await userExists(email)) {
			return res.status(404).json('No user found.')
		}
		let user = await getUserByEmail(email)
		if(!await comparePasswords(password, user.password)) {
			return res.status(400).json('Invalid password')
		}
		let token = await generateJWT({
			userId: user.id,
			role: user.role,
			profile: {
				avatar: user.profile.avatar,
				name: user.profile.name,
				username: user.profile.username,
				profileId: user.profile.id
			}
		})
		return res.json({
			access_token: token
		})
	}
	catch(err) {
		console.log(err)
		return res.sendStatus(500)
	}
}


/**
 * @type {import("express").RequestHandler}
 */
export const getUserInfoController = async (req, res, next) => {
	const { payload } = req.locals
	try {
		return res.json(payload)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}


/**
 * @type {import("express").RequestHandler}
 */
export const getAllMembersController = async (req, res, next) => {
	try {
		const allMembers = await getListOfMembers()
		if(!allMembers) return res.sendStatus(404)
		return res.json(allMembers)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}


/**
 * @type {import("express").RequestHandler}
 */
export const updatedProfileController = async (req, res, next) => {
	try {
		let data = req.body
		let { userId } = req.locals
		const updatedProfile = await updateProfileById(userId, data)
		if(!updatedProfile) return res.sendStatusResponse(500, 'Could not update profile.')
		return res.json(updatedProfile)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}


/**
 * @type {import("express").RequestHandler}
 */
export const getMemberProfileController = async (req, res, next) => {
	try {
		const { username } = req.params
		const memberProfile = await getMemberProfileByUsername(username)
		if(!memberProfile) {
			return res.sendStatus(404)
		}
		return res.json(memberProfile)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}


/**
 * @type {import("express").RequestHandler}
 */
export const uploadProfilePicController = async (req, res, next) => {
	try {
		const { file } = req
		const { profile: { username }, userId } = req.locals
		const fb = readFileSync(file.path)
		const image = await uploadProfilePic(username, file.filename, fb)
		unlink(file.path, (err) => {
			if(err) {
				console.error('failed to delete')
			}
			console.log('file deleted')
		})
		if(image.uploaded) {
			const updatedProfile = await updateProfileById(userId, {
				avatar: image.key
			})
			if(!updatedProfile) throw Error('Cannot update profile')
			return res.json(updatedProfile)
		} else {
			return res.sendStatus(400)
		}
	}
	catch(err) {
		console.log(err)
		res.sendStatus(500)
	}
}
