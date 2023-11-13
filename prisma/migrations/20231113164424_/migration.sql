-- CreateTable
CREATE TABLE "Blog" (
    "id" STRING NOT NULL,
    "title" STRING NOT NULL,
    "tags" STRING[],
    "content" STRING NOT NULL,
    "date" STRING NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Blog_pkey" PRIMARY KEY ("id")
);
