import { comparePasswords, hashPassword } from "../lib/bcrypt/password.js"
import { generateJWT } from "../lib/jose/jwt.js"
import { createUser, getUserByEmail, userExists } from "../repository/user.js"

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
			profileId: user.profile.id
		})
		return res.ok({
			access_token: token
		})
	}
	catch(err) {
		return res.sendStatus(500)
	}
}
