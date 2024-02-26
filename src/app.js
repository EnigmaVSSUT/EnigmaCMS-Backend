import express, { json, urlencoded } from "express";
import 'dotenv/config'
import cors from 'cors'
import morgan from "morgan";
import appRouter from "./app/index.js";

const port = process.env.PORT

const whitelist = [
	'http://127.0.0.1:4000',
	'http://127.0.0.1:3000',
	'https://apply.enigmavssut.com',
	'https://enigmavssut.com',
	'https://club.enigmavssut.com',
	'https://enigma-dev-web.web.app',
	'https://enigma-web-preview.web.app',
	'https://dev.enigmavssut.com'
]

const app = express()

app.use(morgan('dev'))
app.use(cors({
	origin: function(origin, callback) {
		// console.log('origin', origin)
		if (whitelist.indexOf(origin) !== -1 || !origin) {
			callback(null, true)
		} else {
			callback(new Error('Not allowed by CORS'))
		}
	}
}))
app.use(json())
app.use(urlencoded({
	extended: true
}))

app.use(appRouter)

app.use((err, req, res, next) => {
	console.error(err.stack)
	res.status(500).json('Server Error')
})

app.listen(port, () => {
	console.log('server: Server listening on port', port)
})

export default app
