import React, { Component, Fragment } from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import api from '../api-proxy'

import Footer from './Footer'
import Header from './Header'

import Menu from './Menu'
import Register from './Register'
import Login from './Login'
import Logout from './Logout'
import ItemCreate from './ItemCreate'
import ItemUpdate from './ItemUpdate'
import ItemDelete from './ItemDelete'
import Cart from './Cart'
import Transactions from './Transactions'

class App extends Component {

	constructor(props) {
		super(props)

		this.state = {
			name: localStorage.getItem('name'),
			role: localStorage.getItem('role'),
			token: localStorage.getItem('token'),
			cartQuantity: 0
		}
	}

	componentDidMount() {
		this.getTotalCartQuantity()
	}

	setUser() {
		this.setState({
			name: localStorage.getItem('name'),
			role: localStorage.getItem('role'),
			token: localStorage.getItem('token')
		})
	}

	unsetUser() {
		localStorage.clear()

		this.setState({
			name: localStorage.getItem('name'),
			role: localStorage.getItem('role'),
			token: localStorage.getItem('token')
		})
	}

	getTotalCartQuantity() {
		let cartQuantity = 0
        let cart = JSON.parse(localStorage.getItem('cart'))

		if (cart != null) {
			for (let i = 0; i < cart.length; i++) {
				cartQuantity += parseFloat(cart[i].quantity) 
			}
		}

		this.setState({ cartQuantity: cartQuantity })
    }

	render() {
		let LoginComponent = (props) => (<Login {...props} setUser={ this.setUser.bind(this) }/>)
		let LogoutComponent = (props) => (<Logout {...props} unsetUser={ this.unsetUser.bind(this) }/>)
		let MenuComponent = (props) => (<Menu {...props} getTotalCartQuantity={ this.getTotalCartQuantity.bind(this) }/>)
		let CartComponent = (props) => (<Cart {...props} getTotalCartQuantity={ this.getTotalCartQuantity.bind(this) }/>)

		return (
			<Fragment>
				<BrowserRouter>
					<Header token={ this.state.token } name={ this.state.name } role={ this.state.role } cartQuantity={ this.state.cartQuantity }/>
					<Switch>
						<Route exact path='/' render={ MenuComponent }/>
						<Route exact path='/register' component={ Register }/>
						<Route exact path='/login' render={ LoginComponent }/>
						<Route exact path='/logout' render={ LogoutComponent }/>
						<Route exact path='/item-create' component={ ItemCreate }/>
						<Route exact path='/item-update' component={ ItemUpdate }/>
						<Route exact path='/item-delete' component={ ItemDelete }/>
						<Route exact path='/cart' render={ CartComponent }/>
						<Route exact path='/transactions' component={ Transactions }/>
					</Switch>
				</BrowserRouter>
				<Footer/>
			</Fragment>
		)
	}

}

export default App