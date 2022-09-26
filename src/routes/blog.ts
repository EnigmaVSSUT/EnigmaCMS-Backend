
import express, { Router } from 'express';
import blogController from '../controllers/blogController.js';

const router: Router = express.Router()

router.post('/', blogController.addNewBlog)
router.get('/:id', blogController.getBlogById)

export { router as BlogRouter }
