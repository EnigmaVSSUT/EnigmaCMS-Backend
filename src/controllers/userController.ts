import { Prisma, Profile } from "@prisma/client";
import { NextFunction, Request, Response } from "express";
import { verifyPassword } from "../middlewares/bcrypt.js";
import { generateToken } from "../utils/jwt.js";
import prisma from "../utils/prisma.js";

const signUp = async (req: Request, res: Response) => {
	const { email, password } = req.body
	try {
		const newUser = await prisma.user.create({
			data: {
				email,
				password,
				token: {
					create: {
						token: generateToken({
							email: email,
						})
					}
				}
			},
			select: {
				id: true,
				token: true
			}
		})

		res.status(201).json({
			message: 'User created successfully',
			userId: newUser.id,
			token: newUser.token?.token,
		})
	}
	catch(err) {
		console.log('error signup', err)
		if(err instanceof Prisma.PrismaClientKnownRequestError) {
			res.status(400).json({
				error: 'Email already registered',
				message: 'Email already registered'
			})
		} else {
			res.status(500).json({
				error: 'Error creating user',
				message: 'Error creating user'
			})
		}
	}
}

const logIn = async (req: Request, res: Response) => {
	const { email, password } = req.body
	try {
		const user = await prisma.user.findFirst({
			where: {
				email: email
			},
			select: {
				id: true,
				password: true,
				token: true
			}
		})
		const isPasswordValid = await verifyPassword(password, user!.password)
		if(isPasswordValid) {
			if(user?.token) {
				res.status(200).json({
					message: 'Login successful',
					token: user.token.token
				})
			} else {
				const token = await prisma.token.create({
					data: {
						token: generateToken({
							email: email
						}),
						userId: user!.id
					}
				})
				res.status(200).json({
					message: 'Login successful',
					token: token.token
				})
			}
		}
		else {
			res.status(400).json({
				error: 'Invalid password',
				message: 'Invalid password',
			})
		}
	}
	catch(err) {
		console.log('error login', err)
		res.status(400).json({
			error: 'User not found',
			message: 'User not found. Please create an account'
		})
	}
}

const logOut = async (req: Request, res: Response) => {
	const user = req.user
	console.log(user)
	try {
		const deletedToken = await prisma.token.delete({
			where: {
				userId: user.id
			}
		})
		res.json({ message: 'Log out successful' })
	}
	catch(err) {
		console.log('error logout', err)
		res.status(500).json({
			message: 'Invalid request'
		})
	}
	
}

const createOrUpdateProfile = async (req: Request, res: Response, next: NextFunction) => {
	const profile: Profile = req.body
	const user = req.user
	if(!user.profile) {
		try {
			const updatedUser = await prisma.user.update({
				data: {
					profile: {
						create: {
							...profile
						}
					}
				},
				where: {
					id: user.id
				},
				select: {
					profile: true
				}
			})
			res.status(201).json({
				message: 'Successfully created profile',
				profile: updatedUser.profile
			})
		}
		catch(err) {
			console.log('error profile', err)
			res.status(500).json({
				error: 'Error creating profile',
				message: 'Error creating profile'
			})
		}
	} else {
		try {
			const updatedUser = await prisma.user.update({
				data: {
					profile: {
						update: {
							...profile
						}
					}
				},
				where: {
					id: user.id
				},
				select: {
					profile: true
				}
			})
			res.status(201).json({
				message: 'Successfully created profile',
				profile: updatedUser.profile
			})
		}
		catch(err) {
			console.log('error profile', err)
			res.status(500).json({
				error: 'Error creating profile',
				message: 'Error creating profile'
			})
		}
	}
}

const userController = {
	signUp,
	logIn,
	logOut,
	createOrUpdateProfile
}

export default userController
