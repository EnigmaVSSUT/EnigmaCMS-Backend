import BlogRepository from './repository.js'

/**
 * @type {import("express").RequestHandler}
 */
const getAll = async (req, res, next) => {
	const allBlogs = await BlogRepository.getAll()
	res.json(allBlogs)
}

/**
 * @type {import("express").RequestHandler}
 */
const getDetail = async (req, res, next) => {
	try {
		const { slug } = req.params
		const blog = await BlogRepository.getOne(slug)
		res.json(blog)
	}
	catch(err) {
		res.sendStatus(404)
	}
}

/**
 * @type {import("express").RequestHandler}
 */
const create = async (req, res, next) => {
	const blogCreateData = req.body
	try {
		const blog = await BlogRepository.create(blogCreateData)
		res.json(blog)
	}
	catch(err) {
		res.sendStatus(500)
	}
}


/**
 * @type {import('express').RequestHandler}
 */
const update = async (req, res, next) => {
	const blogEditData = req.body
	const {slug} = req.params
	try {
		const updatedBlog = await BlogRepository.update(slug, blogEditData)
		res.json(updatedBlog)
	}
	catch(err) {
		res.sendStatus(400)
	}
}


const BlogController = {
	getAll,
	getDetail,
	create,
	update
}

export default BlogController
