import React, { Component } from 'react'
import { Redirect, Link } from 'react-router-dom'
import api from '../api-proxy'

document.title = 'Cart'

class Cart extends Component {

	constructor(props) {
		super(props)

		this.state = {
			items: [],
			gotoTransactions: false
		}
	}

	componentWillMount() {
		this.getItems()
	}

	getItems() {
		let payload = {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			body: localStorage.getItem('cart')
		}

		fetch(api.url + '/cart/info', payload)
		.then((response) => response.json())
		.then((cartItems) => {
			console.log(cartItems)
			this.setState({ items: cartItems })
		})
	}

	emptyCart() {
		localStorage.removeItem('cart')
		this.props.getTotalCartQuantity()
		this.setState({ items: [] })
	}

	proceedToCheckout() {
		let cart = localStorage.getItem('cart')

		let payload = {
			method: 'post',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': localStorage.getItem('token')
			},
			body: JSON.stringify({
				cart: cart
			})
		}

		fetch(api.url + '/cart/checkout', payload)
		.then((response) => response.json())
		.then((response) => {
			if (response.result == 'success') {
				this.setState({ gotoTransactions: true })
				this.emptyCart()
			} else {
				alert(response.error)
			}
		})
	}

	proceedToStripeCheckout() {
		let cart = localStorage.getItem('cart')

		let payload = {
			method: 'post',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': localStorage.getItem('token')
			},
			body: JSON.stringify({
				cart: cart
			})
		}

		fetch(api.url + '/cart/checkout-stripe', payload)
		.then((response) => response.json())
		.then((response) => {
			if (response.result == 'success') {
				this.setState({ gotoTransactions: true })
				this.emptyCart()
			} else {
				alert(response.error)
			}
		})
	}

	render() {
		if (this.state.gotoTransactions) {
			return <Redirect to='/transactions'/>
		}

		if (this.state.items.length == 0) {
			return (
				<div className="container-fluid mt-3">
					<h3> No items in cart. </h3>
					<h4> Select a menu item to add to cart from <Link to="/">here</Link>.</h4>
				</div>
			)
		}

		let totalPrice = 0;

		this.state.items.map((item) => {
			totalPrice += (item.quantity * item.unitPrice)
		})

		return (
			<div className="container-fluid mt-3">

				<h3>Cart</h3>

				<table className="table table-bordered">

					<thead>

						<tr> 
							<th>Item</th>
							<th>Unit Price</th>
							<th>Quantity</th>
							<th>Subtotal</th>
							<th>Action</th>
						</tr>

					</thead>

					<tbody>

						<CartList getItems={ this.getItems.bind(this) } items={ this.state.items } getTotalCartQuantity={ this.props.getTotalCartQuantity }/>
						
						<tr> 
							<th colSpan="3" className="text-right">Total</th>
							<th className="text-right">&#8369; { totalPrice.toFixed(2) }</th>
							<th></th>
						</tr>

					</tbody>

				</table>

				<button className="btn btn-danger mr-3" onClick={ this.emptyCart.bind(this) }>Empty Cart</button>
				<button className="btn btn-primary mr-3" onClick={ this.proceedToCheckout.bind(this) }>Proceed to Checkout</button>
				<button className="btn btn-primary" onClick={ this.proceedToStripeCheckout.bind(this) }>Proceed to Checkout (Stripe)</button>

			</div>
		)
	}

}

const CartList = (props) => {
	return (
		props.items.map((item) => {
			return (
				<tr key={ item._id }>
					<td>{ item.name }</td>
					<td>&#8369; { (item.unitPrice).toFixed(2) }</td>
					<td>
						<UpdateItemInput getItems={ props.getItems } _id={ item._id } getTotalCartQuantity={ props.getTotalCartQuantity } quantity={ item.quantity }/>
					</td>
					<td className="text-right">&#8369; { (item.unitPrice * item.quantity).toFixed(2) }</td>
					<td>
						<RemoveItemButton getItems={ props.getItems } _id={ item._id } getTotalCartQuantity={ props.getTotalCartQuantity } />
					</td>
				</tr>
			)
		})
	)
}

const RemoveItemButton = (props) => {
	const removeItem = () => {
		let cart = JSON.parse(localStorage.getItem('cart'))

		for (let i = 0; i < cart.length; i++) {
			if (cart[i]._id == props._id) {
				cart.splice(i)
			}
		}

		if (cart.length == 0) {
			localStorage.removeItem('cart')
		} else {
			localStorage.setItem('cart', JSON.stringify(cart))
		}

		props.getTotalCartQuantity()
		props.getItems()
	}

	return (
		<button onClick={ removeItem } className="btn btn-danger">Remove</button>
	)
}

class UpdateItemInput extends Component {

	constructor(props) {
		super(props) 

		this.state = {
			quantity: props.quantity
		}
	}

	updateQuantity(e) {
		let cart = JSON.parse(localStorage.getItem('cart'))

		for (let i = 0; i < cart.length; i++) {
			if (cart[i]._id == this.props._id) {
				cart[i].quantity = parseFloat(e.target.value)
			}
		}

		localStorage.setItem('cart', JSON.stringify(cart))
		
		this.setState({ quantity: e.target.value })
		this.props.getTotalCartQuantity()
        this.props.getItems()
	}

	render() {
		return (
			<input value={ this.state.quantity } onChange={ this.updateQuantity.bind(this) } type="number" className="form-control" min="1"/>
		)
	}

}

export default Cart