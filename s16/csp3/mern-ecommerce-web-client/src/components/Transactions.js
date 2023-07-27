import React, { Component } from 'react'
import api from '../api-proxy'

document.title = 'Transactions'

class Transactions extends Component {

	constructor(props) {
		super(props)

		this.state = {
			orders: []
		}
	}

	componentWillMount() {
		let payload = {
			method: 'get',
			headers: {
				authorization: localStorage.getItem('token')
			}
		}

		fetch(api.url + '/orders/user', payload)
		.then((response) => response.json())
		.then((response) => {
			if (response.error == 'token-auth-failed' || response.error == 'undefined-auth-header') {
				window.location.href = '/login'
			}

			this.setState({ orders: response })
		})
	}

	render() {
		return (
			<div className="container-fluid mt-3">

				<h3>Transactions</h3>

				<table className="table table-bordered">

					<thead>
						<tr>
							<th>Order ID</th>
							<th>Total Price</th>
							<th>Order Datetime</th>
						</tr>
					</thead>

					<tbody>
						{
							this.state.orders.map((order)=> {
								return <tr>
									<td>{ order._id }</td>
									<td className="text-right">{ order.totalPrice.toFixed(2) }</td>
									<td>{ new Date(order.datetimeRecorded).toLocaleString() }</td>
								</tr>
							})
						}
					</tbody>

				</table>
				
			</div>
		)
	}
}

export default Transactions