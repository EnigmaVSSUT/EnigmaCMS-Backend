import db from "../../db/client.js"

export const isSlugAvailable = async (slug) => {
	let count = await db.event.count({
		where: {
			slug: slug
		}
	})
	return count > 0 ? false : true
}

export const createNewEvent = (data) => {
	return db.event.create({
		data: data
	})
}

export const getAllEvents = () => {
	return db.event.findMany()
}
