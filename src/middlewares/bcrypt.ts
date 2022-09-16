import { NextFunction, Request, Response } from "express";
import * as bcrypt from 'bcrypt'

const hashPassword = async (req: Request, res: Response, next: NextFunction) => {
	const { password } = req.body
	const hashedPassword = await bcrypt.hash(password, 10)
	req.body.password = hashedPassword
	next()
}

const verifyPassword = async (plainPassword: string, hashedPassword: string) => {
	const match = await bcrypt.compare(plainPassword, hashedPassword)
	return match
}

export {
	hashPassword,
	verifyPassword
}
