/**
 * @type {import("express").ErrorRequestHandler}
 */
export const errorHandler = (err, req, res) => {
	if(err) {
		console.log('Error: ', err)
	}
	res.status(400).json('Bad Request')
}
