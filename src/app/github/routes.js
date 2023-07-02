import { Router } from "express";
import { authCallbackController } from "./controller.js";

const router = Router()

router.get('/success', authCallbackController)

export default router
