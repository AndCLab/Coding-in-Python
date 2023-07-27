import React from 'react'
import { Redirect } from 'react-router-dom'

const Logout = (props) => {
	props.unsetUser()

	return <Redirect to='/login'/>
}

export default Logout