import { Router } from "express";
import { createUserController, getAllMembersController, getMemberProfileController, getUserInfoController, loginUserController, updatedProfileController, uploadProfilePicController } from "./controller.js";
import { upload } from "../../utils/multer.js";
import { authorize } from "../../utils/auth.js";
import { Role } from "@prisma/client";


const router = Router()

router.post('/signup', createUserController)
router.post('/login', loginUserController)
router.get('/', authorize([Role.Admin, Role.Member]), getUserInfoController)
router.get('/all', getAllMembersController)
router.get('/:username', getMemberProfileController)
router.put('/profileUpdate', authorize([Role.Admin, Role.Member]), updatedProfileController)
router.put('/profile-pic', authorize([Role.Admin, Role.Member]), upload.single('avatar'), uploadProfilePicController)

export default router
