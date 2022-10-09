
import express, { Router } from 'express';
import blogController from '../controllers/blogController.js';

const router: Router = express.Router()

router.post('/', blogController.addNewBlog)
router.get('/', blogController.getAllBlogs)
router.get('/:id', blogController.getBlogById)
router.patch('/:id', blogController.updateBlog)
router.delete('/:id', blogController.deleteBlog)

export { router as BlogRouter }
