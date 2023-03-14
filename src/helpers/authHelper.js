import { verifyJWT } from "../lib/jose/jwt.js"

export const authorizeUser = async (req, res, next) => {
	try {
		let token = req.headers.authorization
		let payload = await verifyJWT(token)
		console.log(payload)
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
