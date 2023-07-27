const jwt = require('jsonwebtoken')
const secret = 'MERN-Ecommerce'

module.exports.verify = (req, res, next) => {
    let header = req.headers.authorization
    console.log(req.headers.authorization)
    
    if (typeof header !== 'undefined') {
        req.token = header.slice(7, header.length)
        
        jwt.verify(req.token, secret, (err, data) => {
            (err) ? res.json({ error: 'token-auth-failed' }) : next()
        })
    } else {
        res.json({ error: 'undefined-auth-header' })
    }
}

module.exports.createToken = (user) => {
    let data = {
        _id: user._id, 
        email: user.email, 
        role: user.role, 
        stripeCustomerId: user.stripeCustomerId
    };

    return jwt.sign(data, secret, { expiresIn: '2h' })
}

module.exports.getId = (authToken) => {
    return getPayload(authToken)._id 
}

module.exports.getStripeCustomerId = (authToken) => {
    return getPayload(authToken).stripeCustomerId 
}

module.exports.getRole = (authToken) => {
    return getPayload(authToken).role 
}

getPayload = (authToken) => {
    return jwt.decode(authToken.slice(7, authToken.length), {complete: true}).payload
}