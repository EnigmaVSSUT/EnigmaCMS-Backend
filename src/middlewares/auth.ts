import { Prisma, User, Profile } from "@prisma/client";
import { NextFunction, Request, Response } from "express";
import prisma from "../utils/prisma.js";

const getCurrentUser = async (req: Request, res: Response, next: NextFunction) => {
	const { authorization } = req.headers
	if(!authorization) {
		res.status(403).json({
			error: 'Not authorized',
			message: 'You are not authorized to access this endpoint'
		})
	} else {
		const token = authorization.split(' ')[1]
		try {
			const user: {
				id: number;
				profile: Profile | null;
			} | null = await prisma.user.findFirstOrThrow({
				where: {
					token: {
						token: token
					}
				},
				select: {
					id: true,
					profile: true
				}
			})
			req.user = user
			next()
		}
		catch (error) {
			res.status(403).json({
				error: 'Invalid token',
				message: 'Please login to continue'
			})
		}
	}
}

export {
	getCurrentUser
}
