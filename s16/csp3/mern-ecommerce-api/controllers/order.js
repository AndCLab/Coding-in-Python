const User = require('../models/user')
const auth = require('../jwt-auth')

module.exports.user = (req, res) => {
	let condition = {
		_id: auth.getId(req.headers.authorization)
	}
	
	User.findOne(condition).exec().then((user) => {
		res.status(200).json(user.orders)
	}).catch((err) => {
		res.status(400).json({ error: err.message })
	})
}