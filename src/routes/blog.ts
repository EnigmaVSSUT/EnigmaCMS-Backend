
import express, { Router } from 'express';
import blogController from '../controllers/blogController.js';

const router: Router = express.Router()

router.post('/', blogController.addNewBlog)

export { router as BlogRouter }
