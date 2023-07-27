import React, { Component } from 'react'
import queryString from 'query-string'
import { Redirect, Link } from 'react-router-dom'
import api from '../api-proxy'

document.title = 'Delete Item'

const ItemDelete = (props) => (
	<div className="container-fluid mt-3">

        <div className="row">

            <div className="col-6 mx-auto">

                <h3 className="text-center">Delete Item</h3>

                <div className="card">

                    <div className="card-header">Item Information</div>

                    <div className="card-body">

                    	<ItemDeleteForm urlParam={ props.location.search } />

                    </div>

                </div>

            </div>

        </div>

    </div>
)

class ItemDeleteForm extends Component {

	constructor(props) {
		super(props)

		let params = queryString.parse(this.props.urlParam)

		this.state = {
			_id: params._id,
			itemName: '',
			description: '',
			unitPrice: '',
			categoryName: undefined,
			categories: [],
			returnToMenu: false
		}
	}

	componentWillMount() {
		fetch(api.url + '/categories')
		.then((response) => response.json())
		.then((categories) => {
			this.setState({ categories: categories })	

			fetch(api.url + '/item/' + this.state._id)
			.then((response) => response.json())
			.then((item) => {
				this.setState({ 
					itemName: item.name,
					description: item.description,
					unitPrice: item.unitPrice,
					categoryName: item.categoryName
				})
			})
		})
	}

	formSubmitHandler(e) {
		e.preventDefault()

		let payload = {
			method: 'delete',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				'_id': this.state._id
			})
		}

		fetch(api.url + '/item', payload)
		.then((response) => response.json())
		.then((response) => {
			if (response.error != null) {
				alert(response.error)
			} else {
				this.setState({ returnToMenu: true })
			}
		})
	}

	render() {
		if (this.state.returnToMenu) {
			return <Redirect to='/'/>
		}

		return (
			<form onSubmit={ this.formSubmitHandler.bind(this) }>

				<div className="form-group">
					<label>Item Name</label>
					<input value={ this.state.itemName } type="text" className="form-control" readOnly/>
				</div>

				<div className="form-group">
					<label>Description</label>
					<input value={ this.state.description } type="text" className="form-control" readOnly/>
				</div>

				<div className="form-group">
					<label>Unit Price</label>
					<input value={ this.state.unitPrice } type="number" className="form-control"  readOnly/>
				</div>

				<div className="form-group">
					<label>Category</label>
					<select value={ this.state.categoryName } className="form-control" readOnly >
						<option value disabled>Select Category</option>
						{
							this.state.categories.map((category) => {
								return <option key={ category.id } value= { category.name }>{ category.name }</option>
							})
						}
					</select>
				</div>

				<button type="submit" className="btn btn-danger btn-block">Delete</button>
				<Link className="btn btn-warning btn-block" to="/">Cancel</Link>

			</form>
		)
	}
}

export default ItemDelete