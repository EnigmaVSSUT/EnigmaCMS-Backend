import { checkEnigmaMembership, getAccessTokenAndUser, setPublicEnigmaMember } from "./repository.js"

/**
 * @type {import("express").RequestHandler}
 */
export const authCallbackController = async (req, res, next) => {
	const { code } = req.query
	try {
		let data = await getAccessTokenAndUser(code)
		if(!await checkEnigmaMembership(data.user, data.accessToken)) {
			return res.status(400).json('User not a member of Enigma VSSUT Organization')
		}
		res.redirect(`${process.env.GITHUB_AUTH_SUCCESS_REDIRECT_URL}?user=${data.user}&accessToken=${data.accessToken}`)
	}
	catch(err) {
		console.log(err)
		res.sendStatus(400)
	}
}
