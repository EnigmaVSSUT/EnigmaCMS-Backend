export const errorHelper = (err, req, res, next) => {
	console.log(err)
	// if(err.code === 'LIMIT_FILE_SIZE')

	res.status(500).json(err.message || 'Server Error. Try again after sometime')
}
