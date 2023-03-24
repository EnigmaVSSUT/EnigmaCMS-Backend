import { ref, uploadBytes, getDownloadURL } from "firebase/storage"
import { storage } from "./init.js"

const profileFolderRef = ref(storage, 'avatar')

export const uploadProfilePic = async (username, filename, file) => {
	try{
		const fileRef = ref(profileFolderRef, filename)
		await uploadBytes(fileRef, file)
		return {
			uploaded: true,
			key: fileRef.fullPath
		}
	}
	catch(err) {
		console.log(err)
		return {
			uploaded: false,
			key: ''
		}
	}
}

export const getImageUrl = async (key) => {
	try {
		const fileRef = ref(storage, key)
		const url = await getDownloadURL(fileRef)
		return url
	}
	catch(err) {
		return null
	}
}
