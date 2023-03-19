import { githubAPIMethods, githubMethods } from "../lib/axios/github.js"

export const getAccessTokenAndUser = async (code) => {
	try {
		let accessToken = (await githubMethods.getAccessToken(code)).data.access_token
		let user = (await githubAPIMethods.getAuthenticatedUser(accessToken)).data.login
		return {
			accessToken,
			user
		}
	}
	catch(err) {
		throw err
	}
}

export const checkEnigmaMembership = async (username, accessToken) => {
	try {
		let response = await githubAPIMethods.checkEnigmaMembership(username, accessToken)
		if(response.status === 204)
			return true
		else 
			return false
	}
	catch(err) {
		return false
	}
}

export const setPublicEnigmaMember = async (username, accessToken) => {
	try {
		console.log(accessToken)
		await githubAPIMethods.setPublicMember(username, accessToken)
		console.log('set public member')
		return true
	}
	catch(err) {
		console.log('failed to set public member')
		console.log(err.response.data)
		return false
	}
}
