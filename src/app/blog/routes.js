import { Router } from "express";
import { saveBlogController, getBlogsController, getParticularBlogController, updateBlogController,deleteBlogController} from "./controller.js";
import { authorize } from "../../utils/auth.js";
import { Role } from "@prisma/client";

const router = Router()

router.post('/create', authorize([Role.Admin]), saveBlogController)
router.get('/getBlogs', getBlogsController);
router.get('/getBlogById/:blogId', getParticularBlogController);
router.put('/updateBlog', authorize([Role.Admin]), updateBlogController);
router.delete('/deleteBlogById/:blogId', authorize([Role.Admin]), deleteBlogController);
export default router;
