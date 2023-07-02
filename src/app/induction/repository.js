import db from "../../db/client.js"

export const createInduction = (induction) => {
	return db.induction.create({
		data: induction
	})
} 

export const inductionExistsByEmail = async (email) => {
	let count = await db.induction.count({
		where: {
			email: email
		}
	})
	return count > 0 ? true : false
}

export const inductionExistsByWhatsAppNumber = async (whatsapp_no) => {
	let count = await db.induction.count({
		where: {
			whatsapp_no: whatsapp_no
		}
	})
	return count > 0 ? true : false
}

export const inductionExistsByGitHub = async (github_profile_url) => {
	let count = await db.induction.count({
		where: {
			github_profile_url: github_profile_url
		}
	})
	return count > 0 ? true : false
}

export const inductionExistsByHackerEarth = async (hackerearth_profile_url) => {
	let count = await db.induction.count({
		where: {
			hackerearth_profile_url: hackerearth_profile_url
		}
	})
	return count > 0 ? true : false
}

export const getAllInductions = () => {
	return db.induction.findMany()
}

export const getInductionById = (id) => {
	return db.induction.findFirstOrThrow({
		where: {
			id: id
		}
	})
}

export const editInductionById = (id, data) => {
	return db.induction.update({
		where: {
			id: id
		},
		data: data
	})
}
