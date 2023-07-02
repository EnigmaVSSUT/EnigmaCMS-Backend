/*
  Warnings:

  - Changed the type of `content` on the `Blog` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- AlterTable
ALTER TABLE "Blog" DROP COLUMN "content";
ALTER TABLE "Blog" ADD COLUMN     "content" JSONB NOT NULL;
