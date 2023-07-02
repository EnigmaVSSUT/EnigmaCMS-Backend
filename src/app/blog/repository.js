import { Prisma } from "@prisma/client"
import db from "../../db/client.js"

const getAll = () => {
	return db.blog.findMany({
		select: {
			id: true,
			title: true,
			slug: true,
			bannerImage: true,
			author: {
				select: {
					name: true,
					avatar: true,
					username: true,
				}
			},
			createdAt: true,
			category: true,
			status: true
		},
		orderBy: {
			createdAt: 'desc'
		}
	})
}

/**
 * 
 * @param {string} slug 
 */
const getOne = (slug) => {
	return db.blog.findFirstOrThrow({
		where: {
			slug: slug
		},
		include: {
			author: {
				select: {
					avatar: true,
					name: true,
					username: true,
					linkedin_url: true,
					twitter_username: true
				}
			},
			category: true
		}
	})
}

/**
 * 
 * @param {Prisma.BlogCreateInput} blogData 
 */
const create = (blogData) => {
	return db.blog.create({
		data: blogData
	})
}

/**
 * 
 * @param {string} slug 
 * @param {Prisma.BlogUpdateInput} data  
 */
const update = (slug, data) => {
	return db.blog.update({
		where: {
			slug: slug
		},
		data: data
	})
}


const BlogRepository = {
	getAll,
	getOne,
	update,
	create
}

export default BlogRepository
