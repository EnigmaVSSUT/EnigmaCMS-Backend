import express, { Request, Response, Express } from 'express'
import * as dotenv from 'dotenv'
import { userRouter } from './routes/user.js'
import { BlogRouter } from './routes/blog.js'

dotenv.config()
const app: Express = express()

const port = process.env.PORT

app.use(express.json())

app.use('/status', (req: Request, res: Response) => {
	res.json({
		message: 'server running'
	})
})

app.use('/user', userRouter)
app.use('/blog', BlogRouter)

app.listen(port, () => {
	console.log('server listening on port', port)
})
