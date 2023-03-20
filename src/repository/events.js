import prisma from "../lib/prisma/client.js"

export const isSlugAvailable = async (slug) => {
	try {
		let count = await prisma.event.count({
			where: {
				slug: slug
			}
		})
		return count > 0 ? false : true
	}
	catch(err) {
		return false
	}
}

export const createNewEvent = async (data) => {
	try {
		const newEvent = await prisma.event.create({
			data: data
		})
		return newEvent
	}
	catch(err) {
		console.log(err)
		return null
	}
}

export const getAllEvents = async () => {
	try {
		const allEvents = await prisma.event.findMany()
		return allEvents
	}
	catch(err) {
		return null
	}
}
