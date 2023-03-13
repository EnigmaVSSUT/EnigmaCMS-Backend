import { Router } from "express";
import githubRouter from "./github.js";
import userRouter from "./user.js";
import { authorizeUser } from "../helpers/authHelper.js";

const appRoutes = Router()

appRoutes.get('/status', (req, res, next) => {
	res.sendStatus(200)
})
appRoutes.use('/github', githubRouter)
appRoutes.use('/user', userRouter)

export default appRoutes
