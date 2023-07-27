// Declare dependencies.

const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')

require('dotenv').config()

// Declare constants.

const app = express()
const defaultPort = 4000
const designatedPort = process.env.PORT || defaultPort

// Declare middlewares.

app.use(bodyParser.json())

// Enable the Cross Origin Resource Sharing (CORS).

app.use(function(req, res, next) {
	res.header('Access-Control-Allow-Origin', '*')
	res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization')
	res.header('Access-Control-Allow-Methods', 'PUT, POST, GET, DELETE, OPTIONS')
	next()
})

// Declare database connection.

mongoose.connect(process.env.MONGODB_SRV, { useNewUrlParser:true, useCreateIndex: true })
mongoose.connection.once('open', () => {
	console.log('Connection to MongoDB Atlas has been successfully tested.')
}).catch(function(err) {
	console.log(err)
})

// Declare routes.

app.use('/api', require('./routes'))

// Listen to server requests.

app.listen(designatedPort, () => {
	console.log('Node.js backend now online in port ' + designatedPort)
})