import jwt from 'jsonwebtoken'

const secret = process.env.JWT_SECRET

interface Payload {
	email: string
}

const generateToken = (payload: Payload) => {
	const token = jwt.sign(payload, secret!)
	return token
}

export {
	generateToken
}

