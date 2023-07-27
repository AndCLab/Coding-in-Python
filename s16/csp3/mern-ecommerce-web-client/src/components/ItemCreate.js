import React, { Component, Fragment } from 'react'
import { Redirect } from 'react-router-dom'
import api from '../api-proxy'

document.title = 'Create Item'

const ItemCreate = () => (
	<div className="container-fluid mt-3">

		<div className="row">

			<div className="col-6 mx-auto">

				<h3 className="text-center">Add Item</h3>

				<div className="card">

					<div className="card-header">Item Information</div>

					<div className="card-body">

						<ItemCreateForm/>

					</div>

				</div>

			</div>

		</div>

	</div>
)

class ItemCreateForm extends Component {

	constructor(props) {
		super(props)

		this.fileInput = React.createRef()

		this.state = {
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
		})
	}

	itemNameChangeHandler(e) {
		this.setState({ itemName: e.target.value })
	}

	descriptionChangeHandler(e) {
		this.setState({ description: e.target.value })
	}

	unitPriceChangeHandler(e) {
		this.setState({ unitPrice: e.target.value })
	}

	categoryNameChangeHandler(e) {
		this.setState({ categoryName: e.target.value })
	}

	formSubmitHandler(e) {
		e.preventDefault()

		let payload = {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				name: this.state.itemName,
				description: this.state.description,
				unitPrice: this.state.unitPrice,
				categoryName: this.state.categoryName,
				isArchived: 0
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
					<input value={ this.state.itemName } onChange={ this.itemNameChangeHandler.bind(this) } type="text" className="form-control" required/>
				</div>

				<div className="form-group">
					<label>Description</label>
					<input value={ this.state.description } onChange={ this.descriptionChangeHandler.bind(this) } type="text" className="form-control"/>
				</div>

				<div className="form-group">
					<label>Unit Price</label>
					<input value={ this.state.unitPrice } onChange={ this.unitPriceChangeHandler.bind(this) } type="number" className="form-control" required/>
				</div>

				<div className="form-group">
					<label>Category</label>
					<select value={ this.state.categoryName } onChange={ this.categoryNameChangeHandler.bind(this) } className="form-control" >
						<option value selected disabled>Select Category</option>
						{
							this.state.categories.map((category) => {
								return <option key={ category._id } value={ category.name }>{ category.name }</option>
							})
						}
					</select>
				</div>

				<div className="form-group">
					<label>Image</label>
					<input type="file" className="form-control" ref={ this.fileInput }/>
				</div>

				<button type="submit" className="btn btn-success btn-block">Add</button>

			</form>
		)
	}

}

export default ItemCreate