import { PrismaClient } from "@prisma/client";
import * as dotenv from 'dotenv'

dotenv.config()

const prisma: PrismaClient = new PrismaClient({
	datasources: {
		db: {
			url: process.env.DATABASE_URL
		}
	}
})

export default prisma
