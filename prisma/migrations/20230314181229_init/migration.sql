-- CreateEnum
CREATE TYPE "Role" AS ENUM ('Admin', 'Member');

-- CreateEnum
CREATE TYPE "Gender" AS ENUM ('Male', 'Female', 'PreferNotToSay');

-- CreateTable
CREATE TABLE "User" (
    "id" STRING NOT NULL,
    "email" STRING NOT NULL,
    "password" STRING NOT NULL,
    "role" "Role" NOT NULL DEFAULT 'Member',
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Profile" (
    "id" STRING NOT NULL,
    "name" STRING NOT NULL,
    "username" STRING NOT NULL,
    "graduation_year" INT4 NOT NULL,
    "avatar" STRING,
    "twitter_username" STRING,
    "linkedin_url" STRING,
    "userId" STRING NOT NULL,

    CONSTRAINT "Profile_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Event" (
    "id" STRING NOT NULL,
    "name" STRING NOT NULL,
    "slug" STRING NOT NULL,
    "poster" STRING NOT NULL,
    "subtitle" STRING,
    "description" STRING NOT NULL,
    "is_single_day" BOOL NOT NULL,
    "start_date" TIMESTAMP(3) NOT NULL,
    "end_date" TIMESTAMP(3),
    "registration_start_date" TIMESTAMP(3) NOT NULL,
    "registration_end_date" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Event_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EventRegistration" (
    "id" STRING NOT NULL,
    "name" STRING NOT NULL,
    "gender" "Gender" NOT NULL DEFAULT 'PreferNotToSay',
    "email" STRING NOT NULL,
    "whatsapp_no" STRING NOT NULL,
    "registration_no" STRING NOT NULL,
    "branch" STRING NOT NULL,
    "graduation_year" INT4 NOT NULL,
    "expectations" STRING,
    "eventId" STRING NOT NULL,

    CONSTRAINT "EventRegistration_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Induction" (
    "id" STRING NOT NULL,
    "name" STRING NOT NULL,
    "gender" "Gender" NOT NULL DEFAULT 'PreferNotToSay',
    "email" STRING NOT NULL,
    "whatsapp_no" STRING NOT NULL,
    "github_profile_url" STRING NOT NULL,
    "hackerearth_profile_url" STRING NOT NULL,
    "registration_no" STRING NOT NULL,
    "branch" STRING NOT NULL,
    "graduation_year" INT4 NOT NULL,
    "why" STRING NOT NULL,
    "preferred_primary_domain" STRING NOT NULL,
    "preferred_secondary_domain" STRING NOT NULL,

    CONSTRAINT "Induction_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Profile_username_key" ON "Profile"("username");

-- CreateIndex
CREATE UNIQUE INDEX "Profile_userId_key" ON "Profile"("userId");

-- CreateIndex
CREATE INDEX "Profile_username_idx" ON "Profile"("username");

-- CreateIndex
CREATE UNIQUE INDEX "Event_slug_key" ON "Event"("slug");

-- CreateIndex
CREATE UNIQUE INDEX "Induction_email_key" ON "Induction"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Induction_whatsapp_no_key" ON "Induction"("whatsapp_no");

-- CreateIndex
CREATE UNIQUE INDEX "Induction_github_profile_url_key" ON "Induction"("github_profile_url");

-- CreateIndex
CREATE UNIQUE INDEX "Induction_hackerearth_profile_url_key" ON "Induction"("hackerearth_profile_url");

-- AddForeignKey
ALTER TABLE "Profile" ADD CONSTRAINT "Profile_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EventRegistration" ADD CONSTRAINT "EventRegistration_eventId_fkey" FOREIGN KEY ("eventId") REFERENCES "Event"("id") ON DELETE CASCADE ON UPDATE CASCADE;
