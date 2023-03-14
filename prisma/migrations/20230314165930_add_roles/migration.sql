-- CreateEnum
CREATE TYPE "Role" AS ENUM ('Admin', 'Member');

-- AlterTable
ALTER TABLE "User" ADD COLUMN     "role" "Role" NOT NULL DEFAULT 'Member';
