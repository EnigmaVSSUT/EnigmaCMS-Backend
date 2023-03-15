import { Router } from "express";
import { authCallbackController } from "../controllers/githubController.js";

const githubRouter = Router()

githubRouter.get('/success', authCallbackController)

export default githubRouter
