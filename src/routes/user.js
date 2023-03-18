import { Router } from "express";
import { createUserController, getUserInfoController, loginUserController } from "../controllers/userController.js";
import { authorizeUser } from "../helpers/authHelper.js";

const userRouter = Router()

userRouter.post('/create', createUserController)
userRouter.post('/login', loginUserController)
userRouter.get('/', authorizeUser, getUserInfoController)

export default userRouter
