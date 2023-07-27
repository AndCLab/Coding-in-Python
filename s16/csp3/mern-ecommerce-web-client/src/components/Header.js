import React from 'react'
import { Link } from 'react-router-dom'

const Header = (props) => {
	let navRight = (props.token === null) ?
		(
			<React.Fragment>
				<li className="nav-item">
					<Link className="nav-link" to="/login">Login</Link>
				</li>

				<li className="nav-item">
					<Link className="nav-link" to="/register">Register</Link>
				</li>
			</React.Fragment>
		) :
		(
			<React.Fragment>
				<li className="nav-item">
					<Link className="nav-link" to="/">{ props.name }</Link>
				</li>

				<li className="nav-item">
					<Link className="nav-link" to="/transactions">Transactions</Link>
				</li>

				<li className="nav-item">
					<Link className="nav-link" to="/logout">Logout</Link>
				</li>
			</React.Fragment>
		)

	return (
		<nav className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">

			<Link className="navbar-brand" to="/">MERN E-Commerce</Link>

			<button className="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbar">
				<span className="navbar-toggler-icon"></span>
			</button>

			<div className="collapse navbar-collapse" id="navbar">

				<ul className="navbar-nav mr-auto">

					<li className="nav-item">
						<Link className="nav-link" to="/">Menu</Link>
					</li>

					<li className="nav-item">
						<Link className="nav-link" to="/cart">Cart <span className="badge badge-light">{ props.cartQuantity }</span></Link>
					</li>

				</ul>

				<ul className="navbar-nav ml-auto">

					{ navRight }

				</ul>

			</div>

		</nav>
	)
}

export default Header