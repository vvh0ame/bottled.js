class Bottled {
	constructor() {
		this.api = "https://bottledapi-prod.herokuapp.com"
		this.identityToolkitApi = "https://www.googleapis.com/identitytoolkit/v3/relyingparty"
		this.headers = {
			"user-agent": "okhttp/4.9.1"
		}
		this.countryCode = countryCode
		this.apiKey = "AIzaSyBVGohPflbjY1WFwoCkjauvqXWuck3A_AU"
	}


	async login(email, password) {
		const response = await fetch(
			`${this.identityToolkitApi}/verifyPassword?key=${this.apiKey}`, {
				method: "POST",
				body: JSON.stringify({
					email: email,
					password: password,
					returnSecureToken: true
				}),
				headers: this.headers
			})
		const data = await response.json()
		if ("idToken" in data) {
			this.userId = data.localId
			this.idToken = data.idToken
			this.refreshToken = data.refreshToken
			this.headers["token"] = this.idToken
		}
		return data
	}

	async getAccountInfo(isBackOnline = false) {
		const response = await fetch(
			`${this.api}/users/info`, {
				method: "POST",
				body: JSON.stringify({
					is_back_online: isBackOnline
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getConfig() {
		const response = await fetch(
			`${this.api}/users/config`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAllFriends() {
		const response = await fetch(
			`${this.api}/users/all-friends`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async sendBottle(
			content,
			photo = null,
			listRecent = [],
			parchment = "parchemin",
			feather = "feather_default") {
		const response = await fetch(
			`${this.api}/bottles/send`, {
				method: "POST",
				body: JSON.stringify({
					content: content,
					parchment: parchment,
					feather: feather,
					photo: photo,
					list_recent: listRecent
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getDailyHunt() {
		const response = await fetch(
			`${this.api}/users/daily-hunt`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getIslandInfo(islandId, isStatic = true) {
		const response = await fetch(
			`${this.api}/islands/fetch-lounge`, {
				method: "POST",
				body: JSON.stringify({
					island_id: islandId,
					isStatic: isStatic
				}),
				headers: this.headers
			})
		return response.json()
	}

	async discoverIslands(iso = null, category = null,  order = "active") {
		const response = await fetch(
			`${this.api}/islands/discover-new`, {
				method: "POST",
				body: JSON.stringify({
					iso: iso,
					category: category,
					order: order
				}),
				headers: this.headers
			})
		return response.json()
	}

	async sendIslandRequest(islandId, comment = null) {
		const response = await fetch(
			`${this.api}/islands/send-request`, {
				method: "POST",
				body: JSON.stringify({
					island_id: islandId,
					comment: comment
				}),
				headers: this.headers
			})
		return response.json()
	}

	async reportIsland(islandId) {
		const response = await fetch(
			`${this.api}/islands/report`, {
				method: "POST",
				body: JSON.stringify({
					island_id: islandId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getIslandPosts(islandId, order = "latest") {
		const response = await fetch(
			`${this.api}/posts/fetch`, {
				method: "POST",
				body: JSON.stringify({
					island_id: islandId,
					order: order
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getChatInfo(chatId, friendUserId, isFromSearch, isVisible = true) {
		const response = await fetch(
			`${this.api}/chat/fetch`, {
				method: "POST",
				body: JSON.stringify({
					isFromSearch: isFromSearch,
					chat_id: chatId,
					friend_uid: friendUserId,
					isVisible: isVisible
				}),
				headers: this.headers
			})
		return response.json()
	}

	async sendMessage(chatId, friendUserId, name, content) {
		const response = await fetch(
			`${this.api}/chat/send`, {
				method: "POST",
				body: JSON.stringify({
					chat_id: chatId,
					friend_uid: friendUserId,
					isPush: true,
					onesignalId: null,
					name: name,
					msg: {
						id: Math.floor(Date.now() / 1000) * 1000,
						from_id: this.userId,
						isLoading: true,
						type: "text",
						date: Math.floor(Date.now() / 1000) * 1000,
						content: content
					}
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getUserProfile(userId) {
		const response = await fetch(
			`${this.api}/users/profile`, {
				method: "POST",
				body: JSON.stringify({
					user_id: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async blockUser(userId) {
		const response = await fetch(
			`${this.api}/users/block`, {
				method: "POST",
				body: JSON.stringify({
					user_id: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async unblockUser(userId) {
		const response = await fetch(
			`${this.api}/users/unblock`, {
				method: "POST",
				body: JSON.stringify({
					user_id: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getIslandsFeed(length, islandQty, latestTs, isDisplayWorld) {
		const response = await fetch(
			`${this.api}/islands/feed-mine`, {
				method: "POST",
				body: JSON.stringify({
					latest_ts: latestTs,
					length: length,
					island_qty: islandQty,
					isDisplayWorld: isDisplayWorld
				}),
				headers: this.headers
			})
		return response.json()
	}

	async translateBottle(content, language) {
		const response = await fetch(
			`${this.api}/bottles/translate`, {
				method: "POST",
				body: JSON.stringify({
					content: content,
					toLang: language
				}),
				headers: this.headers
			})
		return response.json()
	}
 }

module.exports = {Bottled}
