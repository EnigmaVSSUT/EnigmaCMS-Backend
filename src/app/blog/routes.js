import { Router } from "express";
import BlogController from "./controller.js";

const router = Router()

router.get('/', BlogController.getAll)
router.post('/', BlogController.create)
router.get('/:slug', BlogController.getDetail)
router.put('/:slug/edit', BlogController.update)

export default router
