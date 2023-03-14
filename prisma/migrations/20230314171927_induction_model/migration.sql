-- CreateTable
CREATE TABLE "Induction" (
    "id" STRING NOT NULL,
    "name" STRING NOT NULL,
    "gender" "Gender" NOT NULL DEFAULT 'PreferNotToSay',
    "email" STRING NOT NULL,
    "whatsapp_no" INT8 NOT NULL,
    "registration_no" INT8 NOT NULL,
    "branch" STRING NOT NULL,
    "graduation_year" INT4 NOT NULL,
    "why" STRING NOT NULL,
    "preferred_primary_domain" STRING NOT NULL,
    "preferred_secondary_domain" STRING NOT NULL,

    CONSTRAINT "Induction_pkey" PRIMARY KEY ("id")
);
