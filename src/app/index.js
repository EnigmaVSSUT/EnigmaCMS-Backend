import { Router } from "express";
import { userRouter } from "./user/index.js";
import { eventRouter } from "./event/index.js";
import { mediaRouter } from "./media/index.js";
import { inductionRouter } from "./induction/index.js";
import { githubRouter } from "./github/index.js";
import { blogRouter } from "./blog/index.js";

const appRouter = Router()

appRouter.use('/user', userRouter)
appRouter.use('/event', eventRouter)
appRouter.use('/media', mediaRouter)
appRouter.use('/induction', inductionRouter)
appRouter.use('/github', githubRouter)
appRouter.use('/blog', blogRouter)

export default appRouter
