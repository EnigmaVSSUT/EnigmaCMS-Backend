import { comparePasswords, hashPassword } from "../lib/bcrypt/password.js"
import { uploadProfilePic } from "../lib/firebase/utils.js"
import { generateJWT } from "../lib/jose/jwt.js"
import { createUser, getListOfMembers, getMemberProfileByUsername, getUserByEmail, getUserById, updateProfileById, userExists } from "../repository/user.js"
import { readFileSync } from 'fs'

export const createUserController = async (req, res, next) => {
	try {
		let data = req.body
		if(await userExists(data.email)) {
			return res.badRequest('User with email already exists.')
		}
		let hashedPassword = await hashPassword(data.password) 
		data.password = hashedPassword
		if(!await createUser(data)) {
			return res.sendStatusResponse(400, 'User with username already exists.')
		}
		return res.sendStatus(201)
	}
	catch(err) {
		res.sendStatus(500)
	}
}

export const loginUserController = async (req, res, next) => {
	try {
		let { email, password } = req.body
		if(!await userExists(email)) {
			return res.badRequest('No user found.')
		}
		let user = await getUserByEmail(email)
		if(!await comparePasswords(password, user.password)) {
			return res.badRequest('Invalid password')
		}
		let token = await generateJWT({
			userId: user.id,
			profileId: user.profile.id,
			role: user.role
		})
		return res.ok({
			access_token: token
		})
	}
	catch(err) {
		return res.sendStatus(500)
	}
}

export const getUserInfoController = async (req, res, next) => {
	const { userId } = req.locals
	try {
		let user = await getUserById(userId)
		if(!user) {
			return res.sendStatus(404)
		}
		return res.ok(user)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}

export const getAllMembersController = async (req, res, next) => {
	try {
		const allMembers = await getListOfMembers()
		if(!allMembers) return res.sendStatus(404)
		return res.ok(allMembers)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}

export const updatedProfileController = async (req, res, next) => {
	try {
		let data = req.body
		let { userId } = req.locals
		const updatedProfile = await updateProfileById(userId, data)
		if(!updatedProfile) return res.sendStatusResponse(500, 'Could not update profile.')
		return res.ok(updatedProfile)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}

export const getMemberProfileController = async (req, res, next) => {
	try {
		const { username } = req.params
		const memberProfile = await getMemberProfileByUsername(username)
		if(!memberProfile) {
			return res.sendStatus(404)
		}
		return res.ok(memberProfile)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}

export const uploadProfilePicController = async (req, res, next) => {
	try {
		const { file } = req
		const { profile: { username }, userId } = req.locals
		const fb = readFileSync(file.path)
		const image = await uploadProfilePic(username, file.filename, fb)
		if(image.uploaded) {
			const updatedProfile = await updateProfileById(userId, {
				avatar: image.key
			})
			if(!updatedProfile) throw Error('Cannot update profile')
			return res.ok(updatedProfile)
		} else {
			return res.sendStatus(400)
		}
	}
	catch(err) {
		res.sendStatusResponse(500, err.message)
	}
}
