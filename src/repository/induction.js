import prisma from "../lib/prisma/client.js"

export const createInduction = async (induction) => {
	try {
		let newInduction = await prisma.induction.create({
			data: induction
		})
		return true
	}
	catch(err) {
		return false
	}
} 

export const inductionExistsByEmail = async (email) => {
	let count = await prisma.induction.count({
		where: {
			email: email
		}
	})
	return count > 0 ? true : false
}

export const inductionExistsByWhatsAppNumber = async (whatsapp_no) => {
	let count = await prisma.induction.count({
		where: {
			whatsapp_no: whatsapp_no
		}
	})
	return count > 0 ? true : false
}

export const inductionExistsByGitHub = async (github_profile_url) => {
	let count = await prisma.induction.count({
		where: {
			github_profile_url: github_profile_url
		}
	})
	return count > 0 ? true : false
}

export const inductionExistsByHackerEarth = async (hackerearth_profile_url) => {
	let count = await prisma.induction.count({
		where: {
			hackerearth_profile_url: hackerearth_profile_url
		}
	})
	return count > 0 ? true : false
}

export const getAllInductions = async () => {
	try {
		let allInductions = await prisma.induction.findMany()
		return allInductions
	}
	catch(err) {
		return null
	}
}
