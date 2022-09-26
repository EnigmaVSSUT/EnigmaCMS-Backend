import prisma from "../utils/prisma.js";
import { Prisma, Profile } from "@prisma/client";
import { NextFunction, Request, Response } from "express";

const addNewBlog = async (req: Request, res: Response, next: NextFunction) => {
	const blog = req.body
	try {
		const newBlog = await prisma.blog.create({
			data: {
				...blog
			},
			select: {
				id: true
			}
		})

		res.status(201).json({
			message: 'Blog created successfully',
			userId: newBlog.id,
		})
	}
	catch(err) {
		console.log(err)
		res.status(500).json({
			message: 'server error',
			error: 'blog creation failed'
		})
	}
}

const blogController = {
	addNewBlog
}

export default blogController
