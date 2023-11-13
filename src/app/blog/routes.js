import { Router } from "express";
import { saveBlog } from "./controller.js";


const router = Router()

router.post('/create', saveBlog)
// router.get('/', getAllInductionController)

export default router;