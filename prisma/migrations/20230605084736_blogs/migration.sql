-- CreateEnum
CREATE TYPE "BlogStatus" AS ENUM ('Draft', 'Published');

-- CreateTable
CREATE TABLE "Blog" (
    "id" STRING NOT NULL,
    "title" STRING NOT NULL,
    "slug" STRING NOT NULL,
    "bannerImage" STRING,
    "content" STRING NOT NULL,
    "keywords" STRING[],
    "status" "BlogStatus" NOT NULL DEFAULT 'Draft',
    "authorId" STRING,
    "categoryId" STRING,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Blog_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Category" (
    "id" STRING NOT NULL,
    "name" STRING NOT NULL,

    CONSTRAINT "Category_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Blog_slug_key" ON "Blog"("slug");

-- AddForeignKey
ALTER TABLE "Blog" ADD CONSTRAINT "Blog_authorId_fkey" FOREIGN KEY ("authorId") REFERENCES "Profile"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Blog" ADD CONSTRAINT "Blog_categoryId_fkey" FOREIGN KEY ("categoryId") REFERENCES "Category"("id") ON DELETE SET NULL ON UPDATE CASCADE;
