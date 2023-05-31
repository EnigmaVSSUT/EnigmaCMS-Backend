import { getAccessTokenAndUser, setPublicEnigmaMember } from "./repository.js"

export const authCallbackController = async (req, res, next) => {
	const { code } = req.query
	try {
		let data = await getAccessTokenAndUser(code)
		if(!await setPublicEnigmaMember(data.user, data.accessToken)) {
			return res.badRequest('Membership not public')
		}
		res.json(data)
	}
	catch(err) {
		res.sendStatus(400)
	}
}
