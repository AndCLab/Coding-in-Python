import React, { Component } from 'react'
import queryString from 'query-string'
import { Redirect } from 'react-router-dom'
import api from '../api-proxy'

document.title = 'Login'

const Login = (props) => {
	if (localStorage.getItem('token') != null) {
		return <Redirect to='/'/>
	}

	return (
		<div className="container-fluid mt-3">

			<div className="row">

				<div className="col-6 mx-auto">

					<h3 className="text-center">Login</h3>

					<div className="card">
					
						<div className="card-header">Enter Login Information</div>

						<div className="card-body">

							<LoginForm urlParam={ props.location.search } setUser={ props.setUser }/>	
							
						</div>

					</div>

				</div>

			</div>
		
		</div>
	)
}

class LoginForm extends Component {

	constructor(props) {
		super(props)

		this.state = {
			email:'',
			password:'',
			errorMessage:'',
			gotoMenu: false
		}
	}

	emailChangeHandler(e) {
		this.setState({ email: e.target.value })
	}

	passwordChangeHandler(e) {
		this.setState({ password: e.target.value })
	}

	formSubmitHandler(e) {
		e.preventDefault()

		let payload = { 
			method: 'post', 
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				'email': this.state.email,
				'password': this.state.password
			})
		}

		fetch(api.url + '/user/login', payload)
		.then((response) => response.json())
		.then((response) => {
			if (response.result == 'authenticated') {
				localStorage.setItem('role', response.role)
				localStorage.setItem('name', response.name)
				localStorage.setItem('token', 'Bearer ' + response.token)
				this.props.setUser()
				this.setState({
					gotoMenu: true
				})
			} else {
				this.setState({
					errorMessage: <div className="alert alert-danger">{ response.error }</div>
				})
			}
		})
	}

	render() {
		if (this.state.gotoMenu) {
			return <Redirect to='/'/>
		}

		let url = this.props.urlParam 
		let params = queryString.parse(url)
		let registerSuccessMessage = null
		let message = null

		if (params.register_success) {
			registerSuccessMessage = <div className="alert alert-success">Registration successful, you may now login.</div>
		}

		if (this.state.errorMessage == '' && registerSuccessMessage != null) {
			message = registerSuccessMessage
		} else {
			message = this.state.errorMessage
		}

		return(
			<form onSubmit={ this.formSubmitHandler.bind(this) }>

				{ message }					

				<label>Email</label>
				<input value={ this.state.email } onChange={ this.emailChangeHandler.bind(this) } type="email" className="form-control"></input>

				<label className="mt-2">Password</label>
				<input value={ this.state.password } onChange={ this.passwordChangeHandler.bind(this) } type="password" className="form-control"></input>

				<button type="submit" className="btn btn-success btn-block mt-3">Login</button>

			</form> 
		)
	}
}

export default Login