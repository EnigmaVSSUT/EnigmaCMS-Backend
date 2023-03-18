import { Router } from "express";
import { createInductionController, editInductionByIdController, getAllInductionController, getInductionByIdController } from "../controllers/inductionController.js";
import { authorizeAdmin, authorizeUser } from "../helpers/authHelper.js";

const inductionRouter = Router()

inductionRouter.post('/', createInductionController)
inductionRouter.get('/', authorizeUser, getAllInductionController)
inductionRouter.get('/:id', authorizeUser, getInductionByIdController)
inductionRouter.put('/:id', authorizeAdmin, editInductionByIdController)

export default inductionRouter
