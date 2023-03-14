-- CreateEnum
CREATE TYPE "Gender" AS ENUM ('Male', 'Female', 'PreferNotToSay');

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
    "whatsapp_no" INT8 NOT NULL,
    "registration_no" INT8 NOT NULL,
    "branch" STRING NOT NULL,
    "graduation_year" INT4 NOT NULL,
    "expectations" STRING,
    "eventId" STRING NOT NULL,

    CONSTRAINT "EventRegistration_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Event_slug_key" ON "Event"("slug");

-- AddForeignKey
ALTER TABLE "EventRegistration" ADD CONSTRAINT "EventRegistration_eventId_fkey" FOREIGN KEY ("eventId") REFERENCES "Event"("id") ON DELETE CASCADE ON UPDATE CASCADE;
