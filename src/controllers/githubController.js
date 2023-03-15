import { getAccessTokenAndUser } from "../repository/github.js"

export const authCallbackController = async (req, res, next) => {
	const { code } = req.query
	try {
		let data = await getAccessTokenAndUser(code)
		res.ok(data)
	}
	catch(err) {
		res.sendStatus(400)
	}
}
