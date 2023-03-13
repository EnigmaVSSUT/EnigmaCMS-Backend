export const errorHelper = (err, req, res, next) => {
	res.status(500).json('Server Error. Try again after sometime')
}
