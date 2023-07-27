const User = require('../models/user')
const stripe = require('stripe')('sk_test_7UMpcYtFni9koYkpFIruYXmT00EzMN9ci9')
const bcrypt = require('bcrypt')
const auth = require('../jwt-auth');

module.exports.login = (req, res) => {
	let condition = { email: req.body.email }

	User.findOne(condition).exec().then((user) => {
        bcrypt.compare(req.body.password, user.password, (err, result) => {
            if (err) { return res.status(400).json({ error: err.message }) }

            if (result) {
                return res.status(200).json({
                    result: 'authenticated',
                    role: user.role,
                    name: user.name,
                    token: auth.createToken(user.toObject())
                })
            } else {
                return res.status(400).json({ error: err.message })
            }
        })
    }).catch(err => {
        return res.status(400).json({ error: err.message })
    })
}

module.exports.register = (req, res) => {
	bcrypt.hash(req.body.password, 10, (err, hash) => {
		// In case encryption encountered an error.
        if (err) { return res.status(400).json({ error: err.message }) }

        stripe.customers.create({
            email: req.body.emailAddress,
            source: 'tok_mastercard',
        }, (err, customer) => {
        	// In case Stripe customer creation failed.
            if (err) { return res.status(400).json({ error: err.message }) }
            
            // Provide additional request body information.
            req.body.password = hash
            req.body.stripeCustomerId = customer.id
            req.body.role = 'customer'

            // Create a new user.
            User.create(req.body).then((user) => {
                res.status(200).json({ result: 'success' })
            }).catch(err => {
                res.status(400).json({ error: err.message })
            })
        })
    })
}