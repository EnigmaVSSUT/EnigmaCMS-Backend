import axios from "axios";

const github = axios.create({
	baseURL: 'https://github.com',
	headers: {
		'Accept': 'application/json'
	}
})

const githubAPI = axios.create({
	baseURL: 'https://api.github.com',
	headers: {
		'Accept': 'application/json'
	}
})

const githubMethods = {
	getAccessToken: (code) => github.post('/login/oauth/access_token', undefined, {
		params: {
			client_id: process.env.GITHUB_APP_CLIENT_ID,
			client_secret: process.env.GITHUB_APP_CLIENT_SECRET,
			code: code
		}
	})
}

const githubAPIMethods = {
	getAuthenticatedUser: (accessToken) => githubAPI.get('/user', {
		headers: {
			'Authorization': `Bearer ${accessToken}`
		}
	}),
	setPublicMember: (username, accessToken) => githubAPI.put(`/orgs/EnigmaVSSUT/public_members/${username}`, null, {
		headers: {
			'Authorization': `Bearer ${accessToken}`
		}
	}),
	checkEnigmaMembership: (username, accessToken) => githubAPI.get(`/orgs/EnigmaVSSUT/members/${username}`, {
		headers: {
			'Authorization': `Bearer ${accessToken}`
		}
	})
}

export { githubMethods, githubAPIMethods }
