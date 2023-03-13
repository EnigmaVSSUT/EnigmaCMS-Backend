/*
  Warnings:

  - Made the column `graduation_year` on table `Profile` required. This step will fail if there are existing NULL values in that column.

*/
-- AlterTable
ALTER TABLE "Profile" ALTER COLUMN "graduation_year" SET NOT NULL;
