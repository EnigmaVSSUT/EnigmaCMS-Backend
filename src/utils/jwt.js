import * as jose from 'jose'

const secret = new TextEncoder().encode(process.env.JWT_SECRET)

const alg = 'HS256'


/**
 * @typedef {Object} Payload
 * @property {string} userId
 * @property {string} profileId
 * @property {string} role
 */


/**
 * 
 * @param {Payload} payload 
 * @returns {string} jwt token
 */
export const generateJWT = async (payload) => {
	let jwt = await new jose.SignJWT(payload)
		.setProtectedHeader({
			alg
		})
		.setIssuedAt()
		.setIssuer(process.env.JWT_ISSUER)
		.setAudience(process.env.JWT_AUDIENCE)
		.setExpirationTime('30d')
		.sign(secret)

	return jwt
}


/**
 * 
 * @param {string} token 
 * @returns {Payload | null}
 */
export const verifyJWT = async (token) => {
	return jose.jwtVerify(token, secret)
}

