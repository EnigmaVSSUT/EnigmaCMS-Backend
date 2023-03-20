import { Router } from "express";
import { checkSlugAvailabilityController, createNewEventController, getAllEventsController } from "../controllers/eventController.js";
import { authorizeUser } from "../helpers/authHelper.js";

const eventRouter = Router()

eventRouter.get('/slug/:slug', authorizeUser, checkSlugAvailabilityController)
eventRouter.post('/', authorizeUser, createNewEventController)
eventRouter.get('/', getAllEventsController)

export default eventRouter
