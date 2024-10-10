# bottled.js
Mobile-API for [Bottled](https://play.google.com/store/apps/details?id=com.bottledapp.bottled) social network which is your safe place to make friends all over the world

## Example
```JavaScript
async function main() {
	const { Bottled } = require("./bottled.js")
	const bottled = new Bottled()
	await bottled.login("email", "password")
}

main()
```
