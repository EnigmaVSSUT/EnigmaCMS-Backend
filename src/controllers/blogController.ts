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
	const data = req.body
	// console.log(data)
	try {
		const updatedBlog = await prisma.blog.update({
			where: {
				id: parseInt(id)
			},
			data: {
				...data
			},
		})
		res.json({
			message: 'Blog updated',
			blog: updatedBlog
		})
	}
	catch(err) {
		res.status(404).json({
			error: 'Blog not found',
			message: 'The requested blog does not exist.'
		})
	}
}

const getAllBlogs = async (req: Request, res: Response, next: NextFunction) => {
	const allBlogs = await prisma.blog.findMany({
		include: {
			author: {
				select: {
					firstName: true,
					lastName: true,
					branch: true,
					gender: true,
					profileImage: true,
					graduationYear: true,
				}
			}
		}
	})

	res.json({
		message: 'Fetched all blogs',
		blogs: allBlogs
	})
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

// TODO: Complete the function to delete a blog by given id.
const deleteBlog = async (req: Request, res: Response, next: NextFunction) => {
	const { id } = req.params
	try {
		const deletedBlog = await prisma.blog.delete({
			where: {
				id: parseInt(id)
			}
		})
		res.json({
			message: 'Blog deleted',
			deletedBlog: deletedBlog
		})
	}
	catch (err) {
		res.status(400).json({
			error: 'Blog already deleted or does not exist',
			message: 'Blog already deleted or does not exist'
		})
	}
}

// TODO: Complete the function to schedule a blog using cron-jobs.
const scheduleBlog = async () => {}

const blogController = {
	addNewBlog,
	getBlogById,
	updateBlog,
	getAllBlogs,
	scheduleBlog,
	deleteBlog
}

export default blogController
