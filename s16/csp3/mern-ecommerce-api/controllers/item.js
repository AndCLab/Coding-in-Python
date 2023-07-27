const Item = require('../models/item')

module.exports.all = (req, res) => {
	Item.find({ isArchived: false }).then((items) => {
		res.status(200).json(items)
	}).catch(err => {
		res.status(400).json({ error: err.message })
	})
}

module.exports.detail = (req, res) => {
	let condition = { _id: req.params._id }

	Item.findOne(condition).exec().then((item) => {
		res.status(200).json(item)
	}).catch(err => {
        res.status(400).json({ error: err.message })
    })
}

module.exports.new = (req, res) => {
	Item.create(req.body).then((item) => {
		res.status(200).json({ result: 'success' })
	}).catch((err) => {
		res.status(400).json({ error: err.message })
	})
}

module.exports.update = (req, res) => {
	let searchParam = { _id: req.body._id }
	let updateParam = req.body

	Item.findOneAndUpdate(searchParam, updateParam, (item) => {
		res.status(200).json({ result: 'success' })
	}).catch((err) => {	
		res.status(400).json({ error: err.message })
	})
}

module.exports.delete = (req, res) => {
	let searchParam = { _id: req.body._id }
	let updateParam = { isArchived: true }

	Item.findOneAndUpdate(searchParam, updateParam, (item) => {
		res.status(200).json({ result: 'success' })
	}).catch((err) => {	
		res.status(400).json({ error: err.message })
	})
}