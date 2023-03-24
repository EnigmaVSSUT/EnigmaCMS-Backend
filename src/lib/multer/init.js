import multer, { diskStorage } from 'multer'

const storage = diskStorage({
	destination: function(req, file, cb) {
		cb(null, 'uploads')
	},
	filename: function(req, file, cb) {
		const { profile } = req.locals
		const fn = profile.username + '.' + file.originalname.split('.').slice(-1)[0]
		cb(null, fn)
	}
})

export const upload = multer({
	storage: storage,
	limits: {
		fileSize: 524288
	}
})
