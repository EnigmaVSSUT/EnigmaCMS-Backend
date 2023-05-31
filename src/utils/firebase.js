import { initializeApp } from "firebase/app"
import { getStorage } from 'firebase/storage'
import { ref, uploadBytes, getDownloadURL } from "firebase/storage"


// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.FIREBASE_API_KEY,
  authDomain: process.env.FIREBASE_AUTH_DOMAIN,
  projectId: process.env.FIREBASE_PROJECT_ID,
  storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.FIREBASE_APP_ID
}

// Initialize Firebase
const app = initializeApp(firebaseConfig)


// Storage
const storage = getStorage(app)
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
