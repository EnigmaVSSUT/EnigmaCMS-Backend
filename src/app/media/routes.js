import { Router } from "express";
import { getImageUrlController } from "./controller.js";

const router = Router()

router.get('/:folder/:file', getImageUrlController)

export default router
