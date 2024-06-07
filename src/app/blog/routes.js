import { Router } from "express";
import { saveBlog } from "./controller.js";
import { getBlogs } from './controller.js';

const router = Router()

router.post('/create', saveBlog)
router.get('/getBlogs', getBlogs);

export default router;
