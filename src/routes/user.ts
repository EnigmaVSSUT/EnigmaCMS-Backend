import express, { Request, Response, Router } from "express";
import userController from "../controllers/userController.js";
import { getCurrentUser } from "../middlewares/auth.js";
import { hashPassword } from "../middlewares/bcrypt.js";

const router: Router = express.Router()

router.post('/signup', hashPassword, userController.signUp)
router.post('/login', userController.logIn)
router.get('/logout', getCurrentUser, userController.logOut)
router.patch('/profile', getCurrentUser, userController.createOrUpdateProfile)

export { router as userRouter }
