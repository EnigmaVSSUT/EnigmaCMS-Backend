/*
  Warnings:

  - A unique constraint covering the columns `[email]` on the table `Induction` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[whatsapp_no]` on the table `Induction` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[github_profile_url]` on the table `Induction` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[hackerearth_profile_url]` on the table `Induction` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `github_profile_url` to the `Induction` table without a default value. This is not possible if the table is not empty.
  - Added the required column `hackerearth_profile_url` to the `Induction` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Induction" ADD COLUMN     "github_profile_url" STRING NOT NULL;
ALTER TABLE "Induction" ADD COLUMN     "hackerearth_profile_url" STRING NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "Induction_email_key" ON "Induction"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Induction_whatsapp_no_key" ON "Induction"("whatsapp_no");

-- CreateIndex
CREATE UNIQUE INDEX "Induction_github_profile_url_key" ON "Induction"("github_profile_url");

-- CreateIndex
CREATE UNIQUE INDEX "Induction_hackerearth_profile_url_key" ON "Induction"("hackerearth_profile_url");
