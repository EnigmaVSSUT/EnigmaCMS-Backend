import { Router } from "express";
import { createInductionController, editInductionByIdController, getAllInductionController, getInductionByIdController } from "./controller.js";
import { Role } from "@prisma/client";
import { authorize } from "../../utils/auth.js";

const router = Router()

router.post('/', createInductionController)
router.get('/', authorize([Role.Admin, Role.Member]), getAllInductionController)
router.get('/:id', authorize([Role.Admin, Role.Member]), getInductionByIdController)
router.put('/:id', authorize([Role.Admin]), editInductionByIdController)

export default router
