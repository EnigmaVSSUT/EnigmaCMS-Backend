import { Router } from "express";
import { createInductionController, getAllInductionController } from "../controllers/inductionController.js";
import { authorizeUser } from "../helpers/authHelper.js";

const inductionRouter = Router()

inductionRouter.post('/', createInductionController)
inductionRouter.get('/', authorizeUser, getAllInductionController)

export default inductionRouter
