const Item = require('../models/item')
const User = require('../models/user')
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY)
const auth = require('../jwt-auth')

module.exports.info = (req, res) => {
	let cart = req.body
	let _ids = []

	for (let i = 0; i < cart.length; i++) {
		_ids.push(cart[i]._id)
	}

	let condition = { '_id': { $in: _ids } }

	Item.find(condition, (err, items) => {
		let cartInfo = []

		for (let i = 0; i < items.length; i++) {
			cartInfo.push({
				_id: items[i]._id,
				name: items[i].name,
				quantity: cart[i].quantity,
				unitPrice: items[i].unitPrice
			})
		}

		res.status(200).json(cartInfo)
	})
}

module.exports.checkout = (req, res) => {
	let userId = auth.getId(req.headers.authorization)
	let cart = JSON.parse(req.body.cart)

	let _ids = []
	let orderItems = []
	let totalPrice = 0

	for (let i = 0; i < cart.length; i++) {
		_ids.push(cart[i]._id)
	}

	Item.find({ '_id': { $in: _ids } }, (err, items) => {
		for (let i = 0; i < items.length; i++) {
			for (let j = 0; j < cart.length; j++) {
				if (items[i]._id == cart[j]._id) {
					orderItems.push({
						_id: items[i]._id,
						name: items[i].name,
						category: items[i].categoryName,
						quantity: cart[j].quantity,
						unitPrice: items[i].unitPrice
					})
					totalPrice += (cart[j].quantity * items[i].unitPrice)
				}
			}
		}

		User.findOne({ _id: userId }).exec().then((user) => {
			let newOrderDoc = user.orders.create({
				datetimeRecorded: new Date(),
				paymentMode: 'Cash on Delivery',
				totalPrice: totalPrice,
				items: orderItems
			})
			user.orders.push(newOrderDoc)
			user.save()
		})
	}).catch((err) => {
		res.status(400).json({ error: err.message })
	})

	res.json({ result: 'success' })
}

module.exports.checkoutStripe = (req, res) => {
	let userId = auth.getId(req.headers.authorization)
	let cart = JSON.parse(req.body.cart)

	let _ids = []
	let orderItems = []
	let totalPrice = 0

	for (let i = 0; i < cart.length; i++) {
		console.log(cart[i])
		_ids.push(cart[i]._id)
	}

	Item.find({ '_id': { $in: _ids } }, (err, items) => {
		for (let i = 0; i < items.length; i++) {
			for (let j = 0; j < cart.length; j++) {
				if (items[i]._id == cart[j]._id) {
					orderItems.push({
						_id: items[i]._id,
						name: items[i].name,
						category: items[i].categoryName,
						quantity: cart[j].quantity,
						unitPrice: items[i].unitPrice
					})
					totalPrice += (cart[j].quantity * items[i].unitPrice)
				}
			}
		}

		stripe.charges.create({
			amount: totalPrice * 100,
			description: null,
			currency: 'php',
			customer: auth.getStripeCustomerId(req.headers.authorization)
		}, (err, charge) => {
			if (err) { return res.status(400).json({ error: err.message }) }

			User.findOne({ _id: userId }).exec().then((user) => {
				let newOrderDoc = user.orders.create({
					datetimeRecorded: new Date(),
					paymentMode: 'Cash on Delivery',
					stripeChargeId: charge.id,
					totalPrice: totalPrice,
					items: orderItems
				})
				user.orders.push(newOrderDoc)
				user.save()
			})

			res.status(200).json({ result: 'success' })
		})
	}).catch((err) => {
		res.status(400).json({ error: err.message })
	})
}