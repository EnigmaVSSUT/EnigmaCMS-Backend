import { Router } from "express";
import githubRouter from "./github.js";
import userRouter from "./user.js";
import { authorizeUser } from "../helpers/authHelper.js";
import inductionRouter from "./induction.js";
import eventRouter from "./events.js";
import CDNRouter from "./cdn.js";

const appRoutes = Router()

appRoutes.get('/status', (req, res, next) => {
	res.sendStatus(200)
})
appRoutes.use('/github', githubRouter)
appRoutes.use('/user', userRouter)
appRoutes.use('/induction', inductionRouter)
appRoutes.use('/event', eventRouter)
appRoutes.use('/cdn', CDNRouter)

export default appRoutes
