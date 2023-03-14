import { createInduction, getAllInductions, inductionExistsByEmail, inductionExistsByGitHub, inductionExistsByHackerEarth, inductionExistsByWhatsAppNumber } from "../repository/induction.js"

export const createInductionController = async (req, res, next) => {
	try {
		let data = req.body
		if(
			await inductionExistsByEmail(data.email) ||
			await inductionExistsByWhatsAppNumber(data.whatsapp_no) ||
			await inductionExistsByGitHub(data.github_profile_url) ||
			await inductionExistsByHackerEarth(data.hackerearth_profile_url)
		) {
			return res.badRequest('You are already registered.')
		}
		if(!await createInduction(data)) {
			return res.sendStatusResponse(500, 'Internal Server Error. Try again later.')
		}
		return res.sendStatus(201)
	}
	catch(err) {
		next(err)
	}
}

export const getAllInductionController = async (req, res, next) => {
	try {
		let allInductions = await getAllInductions()
		return res.ok({
			message: 'All inductions fetched',
			allInductions
		})
	}
	catch(err) {
		console.log(err)
		next(err)
	}
}
