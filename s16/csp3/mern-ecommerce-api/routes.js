// Declare constants.

const express = require('express')
const router = express.Router()
const auth = require('./jwt-auth')

const ItemController = require('./controllers/item')
const CategoryController = require('./controllers/category')
const UserController = require('./controllers/user')
const OrderController = require('./controllers/order')
const CartController = require('./controllers/cart')

// Route declarations.

router.get('/items', ItemController.all)
router.get('/item/:_id', ItemController.detail)
router.post('/item', ItemController.new)
router.put('/item', ItemController.update)
router.delete('/item', ItemController.delete)

router.get('/categories', CategoryController.all)

router.get('/orders/user', auth.verify, OrderController.user)

router.post('/user/login', UserController.login)
router.post('/user/register', UserController.register)

router.post('/cart/info', CartController.info)
router.post('/cart/checkout', CartController.checkout)
router.post('/cart/checkout-stripe', CartController.checkoutStripe)

module.exports = router