import { createNewEvent, getAllEvents, isSlugAvailable } from "../repository/events.js"

export const checkSlugAvailabilityController = async (req, res, next) => {
	try {
		const { slug } = req.params
		if(!await isSlugAvailable(slug)) {
			return res.sendStatus(400)
		} 
		return res.sendStatus(200)
	}
	catch(err) {
		return res.sendStatus(500)
	}
}

export const createNewEventController = async (req, res, next) => {
	try {
		const data = req.body
		const event = await createNewEvent(data)
		if(!event) {
			return res.sendStatus(422)
		}
		return res.ok({
			event
		})
	}
	catch(err) {
		return res.sendStatus(500)
	}
}

export const getAllEventsController = async (req, res, next) => {
	try {
		const allEvents = await getAllEvents()
		return res.ok({
			allEvents
		})
	}
	catch(err) {
		return res.sendStatus(500)
	}
}
