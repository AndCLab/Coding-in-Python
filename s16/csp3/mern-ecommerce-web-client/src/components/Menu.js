import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import api from '../api-proxy'

const Menu = (props) => {
	document.title = 'Menu'
	let btnAddItem = null

	if (localStorage.getItem('role') == 'admin') {
		btnAddItem = <Link className="btn btn-sm btn-primary" to="/item-create">Add Item</Link>
	}
	
	return (
		<div className="container-fluid mt-3">
			<h3>Items on the Menu</h3>
			{ btnAddItem }
			<MenuList getTotalCartQuantity={ props.getTotalCartQuantity }/>
		</div>
	)	
}

class MenuList extends Component {

	constructor(props) {
		super(props)

		this.state = {
			items: []
		}
	}

	componentWillMount() {
		fetch(api.url + '/items')
		.then((response) => response.json())
		.then((items) => {
			this.setState({ items: items })
		})
	}

	render() {
		return (
			<div className="row mt-3">
			{
				this.state.items.map((item) => {
					return (
						<div key={ item._id } className="col-3 mb-3">

							<div className="card">

								<img className="card-img-top" width="100%" height="200px" style={ {objectFit: 'cover'} } src={ item.imageLocation }/>

								<div className="card-body">

									<h4 className="card-title">{ item.name }</h4>

									<p className="card-text">{ item.description }</p>

									<p className="card-text">&#8369;{ item.unitPrice }</p>

									{
										(localStorage.getItem('role') == 'admin') ? 
										(
											<div className="btn-group btn-block">
												<Link className="btn btn-info" to={"/item-update?_id="+item._id }>Edit</Link>
												<Link className="btn btn-danger" to={"/item-delete?_id="+item._id }>Delete</Link>
											</div>
										) : 
										(
											<AddToCartForm _id={ item._id } getTotalCartQuantity={ this.props.getTotalCartQuantity }/>
										)
									}

								</div>

							</div>

						</div>
					)
				})
			}
			</div>
		)
	}
}

class AddToCartForm extends Component {

	constructor(props) {
		super(props)

		this.state = {
			_id: props._id,
			quantity: 0
		}
	}

	quantityChangeHandler(e) {
		this.setState({ quantity: e.target.value })
	}

	formSubmitHandler(e) {
		e.preventDefault()

		let cart = JSON.parse(localStorage.getItem('cart'))

		if (cart != null) {
			for (let i = 0; i < cart.length; i++) {
				if (cart[i]._id == this.state._id) {
					cart[i].quantity = parseFloat(cart[i].quantity) + parseFloat(this.state.quantity)
					
					localStorage.setItem('cart', JSON.stringify(cart))
					alert('Item has been added to cart')

					this.setState({ quantity: 0 })
					this.props.getTotalCartQuantity()

					return
				}
			}

			cart.push({
				'_id': this.state._id,
				'quantity': parseFloat(this.state.quantity)
			})
		} else {
			cart = []
			cart.push({
				'_id': this.state._id,
				'quantity': parseFloat(this.state.quantity)
			})
		}

		localStorage.setItem('cart', JSON.stringify(cart))
		alert('Item has been added to cart')

		this.setState({ quantity: 0 })
		this.props.getTotalCartQuantity()
	}

	render() {
		return (
			<form onSubmit={ this.formSubmitHandler.bind(this) }>
				<div className="input-group">				
					<div className="input-group-prepend">
						<input value={ this.state.quantity } onChange={ this.quantityChangeHandler.bind(this) } type="number" className="form-control" min="1"/>
						<button type="submit" className="btn btn-success btn-add-to-cart">Add</button>
					</div>	
				</div>
			</form>
		)
	}
}

export default Menu