import requests
from time import time

class Bottled:
	def __init__(self, language: str = "ru") -> None:
		self.api = "https://bottledapi-prod.herokuapp.com"
		self.idtk_api = "https://www.googleapis.com/identitytoolkit/v3"
		self.headers = {
			"user-agent": "okhttp/4.9.1"
		}
		self.user_id = None 
		self.access_token = None 
		self.refresh_token = None
		self.idtk_api_key = "AIzaSyBVGohPflbjY1WFwoCkjauvqXWuck3A_AU"
		
	def login(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"email": email,
			"password": password,
			"returnSecureToken": True
		}
		response = requests.post(
			f"{self.idtk_api}/relyingparty/verifyPassword?key={self.idtk_api_key}",
			data=data,
			headers=self.headers).json()
		if "idToken" in response:
			self.user_id = response["localId"]
			self.access_token = response["idToken"]
			self.refresh_token = response["refreshToken"]
			self.headers["token"] = self.access_token
		return response

	def login_with_access_token(
			self,
			access_token: str) -> dict:
		self.access_token = access_token
		self.headers["token"] = self.access_token
		response = self.get_account_info()
		if "uid" in response:
			self.user_id = response["uid"]
		return response

	def get_account_info(
			self,
			is_back_online: bool = False) -> dict:
		data = {
			"isBackOnline": is_back_online
		}
		return requests.post(
			f"{self.api}/users/info",
			data=data,
			headers=self.headers).json()

	def get_config(self) -> dict:
		return requests.post(
			f"{self.api}/users/config",
			headers=self.headers).json()

	def get_all_friends(self) -> dict:
		return requests.post(
			f"{self.api}/users/all-friends",
			headers=self.headers).json()

	def send_bottle(
			self,
			content: str,
			photo: str = None,
			list_recent: list = [],
			parchment: str = "parchemin",
			feather: str = "feather_default") -> dict:
		data = {
			"content": content,
			"parchment": parchment,
			"feather": feather,
			"photo": photo,
			"list_recent": list_recent
		}
		return requests.post(
			f"{self.api}/bottles/send",
			data=data,
			headers=self.headers).json()

	def get_daily_hunt(self) -> dict:
		return requests.post(
			f"{self.api}/users/daily-hunt",
			headers=self.headers).json()

	def edit_profile(
			self,
			bio: str = None,
			name: str = None,
			email: str = None,
			photo: str = None,
			gender: str = None,
			category: str = None,
			interests: list = None,
			languages: list = None) -> dict:
		data = {}
		if bio:
			data["type"] = "bio"
			data["value"] = bio
		elif name:
			data["type"] = "name"
			data["value"] = name
		elif email:
			data["type"] = "email"
			data["value"] = email
		elif photo:
			data["type"] = "photo"
			data["value"] = photo
		elif gender:
			data["type"] = "gender"
			data["value"] = gender
		elif category:
			data["type"] = "category"
			data["value"] = category
		elif interests:
			data["type"] = "interest"
			data["value"] = interests
		elif languages:
			data["type"] = "languages"
			data["value"] = languages
		return requests.post(
			f"{self.api}/users/edit",
			data=data,
			headers=self.headers).json()

	def set_online_status(
			self,
			is_online: bool = True) -> dict:
		data = {
			"isOnline": is_online
		}
		return requests.post(
			f"{self.api}/users/online",
			data=data,
			headers=self.headers).json()

	def delete_notifications(self) -> dict:
		return requests.post(
			f"{self.api}/users/delete-notif",
			headers=self.headers).json()

	def get_island_info(
			self,
			island_id: str,
			is_static: bool = True) -> dict:
		data = {
			"island_id": island_id,
			"isStatic": is_static
		}
		return requests.post(
			f"{self.api}/islands/fetch-lounge",
			headers=self.headers).json()

	def discover_islands(
			self,
			iso: str = None,
			category: str = None,
			order: str = "active") -> dict:
		data = {
			"iso": iso,
			"category": category,
			"order": order
		}
		return requests.post(
			f"{self.api}/islands/discover-new",
			data=data,
			headers=self.headers).json()

	def send_island_request(
			self,
			island_id: str,
			comment: str = None) -> dict:
		data = {
			"island_id": island_id,
			"comment": comment
		}
		return requests.post(
			f"{self.api}/islands/send-request",
			data=data,
			headers=self.headers).json()

	def report_island(
			self,
			island_id: str) -> dict:
		data = {
			"island_id": island_id
		}
		return requests.post(
			f"{self.api}/islands/report",
			data=data,
			headers=self.headers).json()

	def get_island_posts(
			self,
			island_id: str,
			order: str = "latest") -> dict:
		data = {
			"island_id": island_id,
			"order": order
		}
		return requests.post(
			f"{self.api}/posts/fetch",
			data=data,
			headers=self.headers).json()

	def get_chat_info(
			self,
			chat_id: str,
			friend_uid: str,
			is_from_search: bool,
			is_visible: bool = True) -> dict:
		data = {
			"isFromSearch": is_from_search,
			"chat_id": chat_id,
			"friend_uid": friend_uid,
			"isVisible": is_visible
		}
		return requests.post(
			f"{self.api}/chat/fetch",
			data=data,
			headers=self.headers).json()

	def send_message(
			self,
			chat_id: str,
			friend_uid: str,
			content: str) -> dict:
		data = {
			"chat_id": chat_id,
			"friend_uid": friend_uid,
			"isPush": True,
			"onesignalId": None,
			"name": self.name,
			"msg": {
				"id": int(time() * 1000),
				"from_id": self.user_id,
				"isLoading": True,
				"type": "text",
				"date": int(time() * 1000),
				"content": content
			}
		}
		return requests.post(
			f"{self.api}/chat/send",
			data=data,
			headers=self.headers).json()

	def get_user_profile(self, user_id: str) -> dict:
		data = {
			"user_id": user_id
		}
		return requests.post(
			f"{self.api}/users/profile",
			data=data,
			headers=self.headers).json()

	def get_user_photo(self, user_id: str) -> dict:
		data = {
			"userId": user_id
		}
		return requests.post(
			f"{self.api}/users/photo",
			data=data,
			headers=self.headers).json()

	def block_user(self, user_id: str) -> dict:
		data = {
			"user_id": user_id
		}
		return requests.post(
			f"{self.api}/users/block",
			data=data,
			headers=self.headers).json()

	def unblock_user(self, user_id: str) -> dict:
		data = {
			"user_id": user_id
		}
		return requests.post(
			f"{self.api}/users/unblock",
			data=data,
			headers=self.headers).json()

	def get_islands_feed(
			self,
			length: int,
			island_qty: int = 0,
			latest_ts: bool = False,
			is_display_world: bool = False) -> dict:
		data = {
			"latest_ts": latest_ts,
			"length": length,
			"island_qty": island_qty,
			"isDisplayWorld": is_display_world
		}
		return requests.post(
			f"{self.api}/islands/feed-mine",
			data=data,
			headers=self.headers).json()

	def get_post_comments(
			self,
			length: int,
			post_id: str,
			latest_ts: bool = False) -> dict:
		data = {
			"post_id": post_id,
			"latest_ts": latest_ts,
			"length": length
		}
		return requests.post(
			f"{self.api}/comments/fetch",
			data=data,
			headers=self.headers).json()

	def report_post(self, post_id: str) -> dict:
		data = {
			"post_id": post_id
		}
		return requests.post(
			f"{self.api}/posts/report",
			headers=self.headers).json()

	def translate_bottle(
			self,
			content: str,
			language: str) -> dict:
		data = {
			"content": content,
			"toLang": language
		}
		return requests.post(
			f"{self.api}/bottles/translate",
			data=data,
			headers=self.headers).json()

	def search_islands(self, query: str) -> dict:
		data = {
			"search": query
		}
		return requests.post(
			f"{self.api}/islands/search",
			data=data,
			headers=self.headers).json()

	def get_contacts(self, type: str) -> dict:
		data = {
			"type": type
		}
		return requests.post(
			f"{self.api}/users/contact-option",
			data=data,
			headers=self.headers).json()

	def get_account_posts(
			self,
			latest_ts: bool = False) -> dict:
		data = {
			"latest_ts": latest_ts
		}
		return requests.post(
			f"{self.api}/posts/fetch-mine",
			data=data,
			headers=self.headers).json()

	def get_account_comments(
			self,
			latest_ts: bool = False) -> dict:
		data = {
			"latest_ts": latest_ts
		}
		return requests.post(
			f"{self.api}/comments/fetch-mine",
			data=data,
			headers=self.headers).json()

	def get_sent_bottles(self) -> dict:
		return requests.post(
			f"{self.api}/bottles/refresh-sent",
			headers=self.headers).json()

	def get_diaries(
			self,
			days: int,
			nb_friends: int,
			target: str = "world",
			is_first_load: bool = False) -> dict:
		data = {
			"isFirstLoad": is_first_load,
			"target": target,
			"days": days,
			"nb_friends": nb_friends
		}
		return requests.post(
			f"{self.api}/adventures/fetch",
			data=data,
			headers=self.headers).json()

	def get_user_diaries(
			self,
			user_id: str,
			is_private: bool = False,
			latest_ts: bool = False) -> dict:
		data = {
			"from_id": user_id,
			"isPrivate": is_private,
			"latest_ts": latest_ts
		}
		return requests.post(
			f"{self.api}/adventures/user",
			data=data,
			headers=self.headers).json()

	def delete_account(self) -> dict:
		return requests.post(
			f"{self.api}/users/delete",
			data=data,
			headers=self.headers).json()
