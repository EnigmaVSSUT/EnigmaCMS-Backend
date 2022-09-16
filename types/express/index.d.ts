declare namespace Express {
	interface Request {
		user?: (User & {
			profile: Profile | null;
		}) | null
	}
}
