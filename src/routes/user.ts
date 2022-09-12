import express, { Request, Response, Router } from "express";

const router: Router = express.Router()

router.post('/signup', (req: Request, res: Response) => {
	const { email, password } = req.body
	res.status(200).json({
		user: { email, password}
	})
})

export { router as userRouter }
