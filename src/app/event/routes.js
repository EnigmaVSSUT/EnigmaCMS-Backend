import { Router } from "express";
import { checkSlugAvailabilityController, createNewEventController, getAllEventsController } from "./controller.js";
import { authorize } from "../../utils/auth.js";
import { Role } from "@prisma/client";


const router = Router()

router.get('/slug/:slug', authorize([Role.Admin, Role.Member]), checkSlugAvailabilityController)
router.post('/', authorize([Role.Admin, Role.Member]), createNewEventController)
router.get('/', getAllEventsController)

export default router
