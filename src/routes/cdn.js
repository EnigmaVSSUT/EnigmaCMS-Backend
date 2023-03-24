import { Router } from "express";
import { getImageUrlController } from "../controllers/cdnController.js";

const CDNRouter = Router()

CDNRouter.get('/:folder/:file', getImageUrlController)

export default CDNRouter
