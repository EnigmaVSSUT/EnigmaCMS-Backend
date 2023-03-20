import { Router } from "express";
import { createUserController, getAllMembersController, getUserInfoController, loginUserController, updatedProfileController } from "../controllers/userController.js";
import { authorizeSelf, authorizeUser } from "../helpers/authHelper.js";

const userRouter = Router()

userRouter.post('/create', createUserController)
userRouter.post('/login', loginUserController)
userRouter.get('/', authorizeUser, getUserInfoController)
userRouter.get('/all', authorizeUser, getAllMembersController)
userRouter.put('/profile', authorizeUser, updatedProfileController)

export default userRouter
