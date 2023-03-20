import prisma from "../lib/prisma/client.js"

export const createUser = async (data) => {
	try {
		await prisma.user.create({
			data: {
				email: data.email,
				password: data.password,
				profile: {
					create: {
						name: data.profile.name,
						username: data.profile.username,
						graduation_year: data.profile.graduation_year,
						linkedin_url: data.profile.linkedin_url,
						twitter_username: data.profile.twitter_username
					}
				}
			}
		})
		return true
	}
	catch(err) {
		return false
	}
}

export const userExists = async (email) => {
	try {
		let count = await prisma.user.count({
			where: {
				email: email
			}
		})
		// console.log('count', count)
		if(count > 0) return true
		else return false
	}
	catch(err) {
		throw err
	}
}

export const getUserByEmail = async (email) => {
	try {
		let user = await prisma.user.findFirstOrThrow({
			where: {
				email: email
			},
			include: {
				profile: true
			}
		})
		return user
	}
	catch(err) {
		throw err
	}
}

export const getUserById = async (id) => {
	try {
		let user = await prisma.user.findFirstOrThrow({
			where: {
				id: id
			},
			select: {
				email: true,
				role: true,
				profile: {
					select: {
						name: true,
						username: true,
						avatar: true,
						graduation_year: true,
						linkedin_url: true,
						twitter_username: true
					}
				}
			}
		})
		return user
	}
	catch(err) {
		return null
	}
}

export const getListOfMembers = async () => {
	try {
		const allMembers = await prisma.user.findMany({
			select: {
				id: true,
				email: true,
				role: true,
				profile: {
					select: {
						avatar: true,
						graduation_year: true,
						linkedin_url: true,
						name: true,
						twitter_username: true,
						username: true
					}
				}
			}
		})
		return allMembers
	}
	catch(err) {
		return null
	}
}

export const updateProfileById = async (userId, data) => {
	try {
		let updatedProfile = await prisma.profile.update({
			where: {
				userId: userId
			},
			data: data,
			select: {
				name: true,
				username: true,
				avatar: true,
				graduation_year: true,
				linkedin_url: true,
				twitter_username: true
			}
		})
		return updatedProfile
	}
	catch(err) {
		console.error(err)
		return null
	}
}
