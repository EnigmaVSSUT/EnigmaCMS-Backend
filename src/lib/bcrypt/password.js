import { compare, hash } from 'bcrypt'
// import 'dotenv/config.js'

const saltRounds = parseInt(process.env.BCRYPT_SALT_ROUNDS)

export const hashPassword = async (plainPassword) => {
	let hashedPassword =  await hash(plainPassword, saltRounds)
	return hashedPassword
}

export const comparePasswords = async (plainPassword, hashedPassword) => {
	return await compare(plainPassword, hashedPassword)
}
