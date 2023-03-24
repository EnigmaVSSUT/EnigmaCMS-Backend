import { Router } from "express";
import { createUserController, getAllMembersController, getMemberProfileController, getUserInfoController, loginUserController, updatedProfileController, uploadProfilePicController } from "../controllers/userController.js";
import { authorizeAndGetProfile, authorizeUser } from "../helpers/authHelper.js";
import { upload } from "../lib/multer/init.js";

const userRouter = Router()

userRouter.post('/create', createUserController)
userRouter.post('/login', loginUserController)
userRouter.get('/', authorizeUser, getUserInfoController)
userRouter.get('/all', getAllMembersController)
userRouter.get('/:username', getMemberProfileController)
userRouter.put('/profile', authorizeUser, updatedProfileController)
userRouter.put('/profile-pic', authorizeAndGetProfile, upload.single('avatar'), uploadProfilePicController)

export default userRouter
