import { getImageUrl } from "../../utils/firebase.js"


/**
 * @type {import("express").RequestHandler}
 */
export const getImageUrlController = async (req, res, next) => {
	try {
		const { folder, file } = req.params
		const key = `${folder}/${file}`
		const url = await getImageUrl(key)
		if(!url) {
			return res.sendStatus(404)
		}
		res.redirect(url)
	}
	catch(err) {
		next(err)
	}
}
