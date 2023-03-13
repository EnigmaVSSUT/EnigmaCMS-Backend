export const responseHelper = (req, res, next) => {
	res.ok = (data) => res.json(data)
	res.badRequest = (data) => res.status(400).json(data)
	res.notFound = (data) => res.status(404).json(data)
	res.sendStatusResponse = (statusCode, data) => res.status(statusCode).json(data)

	next()
}
