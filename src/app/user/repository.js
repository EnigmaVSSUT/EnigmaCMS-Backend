import db from "../../db/client.js"

export const createUser = (data) => {
	return db.user.create({
		data: {
			email: data.email,
			password: data.password,
			profile: {
				create: {
					name: data.profile.name,
					username: data.profile.username,
					graduation_year: data.profile.graduation_year,
					linkedin_url: data.profile.linkedin_url,
					twitter_username: data.profile.twitter_username,
					domain : data.profile.domain,
					bio: data.profile.bio,
          			skills: data.profile.skills,
          			portfolio_url: data.profile.portfolio_url,
				}
			}
		}
	})
}

export const userExists = async (email) => {
	let count = await db.user.count({
		where: {
			email: email
		}
	})
	return count > 0
}

export const getUserByEmail = (email) => {
	return db.user.findFirstOrThrow({
		where: {
			email: email
		},
		include: {
			profile: true,
		}
	})
}

export const getUserById = (userId) => {
	return db.user.findFirstOrThrow({
		where: {
			id: userId
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
					twitter_username: true,
					domain :true,
					bio: true,
          			skills: true,
          			portfolio_url: true,
				}
			}
		}
	})
}

export const getListOfMembers = () => {
	return db.user.findMany({
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
					username: true,
					domain :true,
					bio: true,
					skills: true,
					portfolio_url: true,
				}
			}
		}
	})
}

export const updateProfileById = async (userId, data) => {
	return db.profile.update({
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
			twitter_username: true,
			domain: true,
			bio: true,
      		skills: true,
      		portfolio_url: true,
		}
	})
}

export const getProfileById = async (profileId) => {
	return db.profile.findFirstOrThrow({
		where: {
			id: profileId
		}
	})
}

export const getMemberProfileByUsername = async (username) => {
	return db.profile.findFirstOrThrow({
		where: {
			username: username
		},
		select: {
			id: true,
			name: true,
			username: true,
			avatar: true,
			graduation_year: true,
			linkedin_url: true,
			twitter_username: true,
			domain:true,
			bio: true,
      		skills: true,
      		portfolio_url: true,
		}
	})
}
