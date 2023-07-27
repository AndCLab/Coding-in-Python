const mongoose = require('mongoose')
const Schema = mongoose.Schema

const UserSchema = new Schema({
    name: {
        type: String,
        required: [true, 'Name is required.']
    },
    email: {
        type: String,
        required: [true, 'Email is required.']
    },
    password: {
        type: String,
        required: [true, 'Pasword is required.']
    },
    role: {
        type: String,
        default: 'customer'
    },
    stripeCustomerId: {
        type: String,
        required: [true, 'Stripe customer ID is required.']
    },
    orders: [
        {
            datetimeRecorded: {
                type: Date,
                default: new Date()
            },
            paymentMode: {
                type: String,
                required: [true, 'Payment mode is required.']
            },
            totalPrice: {
                type: Number,
                required: [true, 'Total price is required.']
            },
            stripeChargeId: {
                type: String,
                default: null
            },
            items: [
                {
                    name: {
                        type: String,
                        required: [true, 'Name is required.']
                    },
                    category: {
                        type: String,
                        required: [true, 'Category is required.']
                    },
                    quantity: {
                        type: Number,
                        require: [true, 'Quantity is required.']
                    },
                    unitPrice: {
                        type: Number,
                        require: [true, 'Unit price is required.']
                    }
                }
            ]
        }
    ]
}, {
    timestamps: true
})

const User = mongoose.model('user', UserSchema)

module.exports = User