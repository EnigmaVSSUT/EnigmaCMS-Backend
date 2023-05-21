import express, { json, urlencoded } from "express";
import 'dotenv/config'
import { errorHelper } from "./helpers/errorHelper.js";
import { responseHelper } from "./helpers/responseHelper.js";
import appRoutes from "./routes/index.js";
import cors from 'cors'
import morgan from "morgan";

const port = process.env.PORT

const whitelist = [
	'http://localhost:3000',
	'http://club.enigma.code:3000',
	'https://apply.enigmavssut.com',
	'https://enigmavssut.com',
	'https://club.enigmavssut.com',
	'https://'
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

app.use(responseHelper)

app.use(appRoutes)

app.use(errorHelper)

app.listen(port, () => {
	console.log('server: Server listening on port', port)
})

export default app
