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

const updateBlog = async (req: Request, res: Response, next: NextFunction) => {
	const { id } = req.params
	try {

	}
	catch(err) {

	}
}

const getBlogById = async (req: Request, res: Response, next: NextFunction) => {
	// console.log(req.params)
	const { id } = req.params
	try {
		const blog = await prisma.blog.findFirstOrThrow({
			where: {
				id: parseInt(id)
			}
		})
		res.status(200).json({
			message: 'Blog fetched successfully',
			blog: blog
		})
	}
	catch(err) {
		res.status(404).json({
			error: 'Blog not found',
			message: 'Blog does not exist'
		})
	}
}

const blogController = {
	addNewBlog,
	getBlogById
}

export default blogController
