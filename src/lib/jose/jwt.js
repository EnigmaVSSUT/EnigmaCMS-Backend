import * as jose from 'jose'

const secret = new TextEncoder().encode(process.env.JWT_SECRET)

const alg = 'HS256'

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

export const verifyJWT = async (token) => {
	try {
		let { payload } = await jose.jwtVerify(token, secret)
		return payload
	}
	catch(err) {
		return null
	}
}

