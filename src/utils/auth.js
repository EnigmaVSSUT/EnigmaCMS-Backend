import { Role } from "@prisma/client"
import { getUserById } from "../app/user/repository.js"
import { verifyJWT } from "./jwt.js"

/**
 * @param {Role[]} roles
 * @returns {import("express").RequestHandler} 
 */
export const authorize = (roles) => async (req, res, next) => {
	if(typeof roles === 'string') {
		roles = [roles]
	}
	const token = req.headers.authorization
	try {
		if(!token) {
			res.status(403).json('No token provided')
		}
		else {
			const tokenParts = token.split(' ')
			if(tokenParts[0] !== 'Bearer') {
				throw Error('Invalid token')
			}
			const { payload } = await verifyJWT(tokenParts[1])
			if(!roles.includes(payload.role)) {
				return res.status(403).json('You don\'t have the permissions to perform this action')
			}
			// const user = await getUserById(payload.userId)
			req.locals = {
				payload
			}
			next()
		}
	}
	catch(err) {
		res.status(403).json('Invalid token')
	}
}
