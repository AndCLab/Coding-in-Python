import React, { Component } from 'react'
import { Redirect } from 'react-router-dom'
import api from '../api-proxy'

document.title = 'Register'

const Register = () => {
	if (localStorage.getItem('token') != null) {
		return <Redirect to='/'/>
	}

	return (
		<div className="container-fluid mt-3">

			<div className="row">
			
				<div className="col-6 mx-auto">
					
					<h3 className="text-center">Registration Page</h3>

					<div className="card">
						
						<div className="card-header">Registration Information</div>

							<div className="card-body">
								
								<RegisterForm/>

							</div>

					</div>			

				</div>

			</div>
			
		</div>
	)
}

class RegisterForm extends Component {

	constructor(props) {
		super(props)

		this.state = {
			name:'',
			email:'',
			password:'',
			gotoLogin: false,
			isSubmitDisabled: true
		}
	}

	nameChangeHandler(e) {
		this.setState({ name: e.target.value })
	}

	emailChangeHandler(e) {
		this.setState({ email: e.target.value })
	}

	passwordChangeHandler(e) {
		if (e.target.value.length < 8) {
			this.setState({ isSubmitDisabled: true })
		} else {
			this.setState({ isSubmitDisabled: false })
		}

		this.setState({ password: e.target.value })
	}

	formSubmitHandler(e) {
		e.preventDefault()

		let payload = {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				'name': this.state.name,
				'email': this.state.email,
				'password': this.state.password
			})
		}

		fetch(api.url + '/user/register', payload)
		.then((response) => response.json())
		.then((response) => {
			if (response.error != null) {
				alert(response.error)
			} else {
				this.setState({ gotoLogin: true })
			}
		})
	}

	render() {
		if (this.state.gotoLogin) {
			return <Redirect to='/login?register_success=true'/>
		}

		return (
			<form onSubmit= { this.formSubmitHandler.bind(this) }>

				<div className="form-group">					
					<label>Name</label>
					<input value={ this.state.name } onChange= { this.nameChangeHandler.bind(this) } type="text" className="form-control mb-1"/>
					<span className="text-danger"></span>
				</div>

				<div className="form-group">					
					<label>Email</label>
					<input value= { this.state.email } onChange={ this.emailChangeHandler.bind(this) } type="email" className="form-control mb-1"/>
					<span className="text-danger"></span>
				</div>


				<div className="form-group">					
					<label>Password</label>
					<input value= { this.state.password } onChange={ this.passwordChangeHandler.bind(this) } type="password" className="form-control mb-1"/>
					<span className="text-danger"></span>
				</div>

				<button disabled={ this.state.isSubmitDisabled } type="submit" className="btn btn-success btn-block">Register</button>

			</form>
		)
	}

}

export default Register