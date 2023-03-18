import { verifyJWT } from "../lib/jose/jwt.js"

export const authorizeUser = async (req, res, next) => {
	try {
		let token = req.headers.authorization
		let payload = await verifyJWT(token)
		// console.log(payload)
		req.locals = {
			userId: payload.userId,
			profileId: payload.profileId,
			role: payload.role
		}
		next()
	}
	catch(err) {
		return res.sendStatus(403)
	}
}

export const authorizeAdmin = async (req, res, next) => {
	try {
		let token = req.headers.authorization
		let payload = await verifyJWT(token)
		// console.log(payload)
		if(payload.role != 'Admin') throw Error('Not an admin')
		req.locals = {
			userId: payload.userId,
			profileId: payload.profileId,
			role: payload.role
		}
		next()
	}
	catch(err) {
		console.log(err)
		return res.sendStatusResponse(403, 'You need to be an admin to perform this action.')
	}
}
