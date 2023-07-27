const mongoose = require('mongoose')
const Schema = mongoose.Schema

const ItemSchema = new Schema({
	name: {
		type: String,
		required: [true, 'Item name is required.']
	},
	description: {
		type: String,
		required: [true, 'Description is required.']
	},
	unitPrice: {
		type: Number,
		required: [true, 'Unit price is required.']
	},
	imageLocation: {
		type: String
	},
	categoryName: {
		type: String,
		required: [true, 'Category name is required.']
	},
	isArchived: {
		type: Boolean,
		required: [true, 'Archive status is required.']
	}
})

const Item = mongoose.model('item', ItemSchema)

module.exports = Item