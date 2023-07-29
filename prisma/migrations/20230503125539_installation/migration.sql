-- CreateTable
CREATE TABLE "SlackInstallation" (
    "app_id" TEXT,
    "team_id" TEXT NOT NULL,
    "team_name" TEXT,
    "enterprise_id" TEXT,
    "enterprise_name" TEXT,
    "is_enterprise_install" BOOLEAN NOT NULL DEFAULT false,
    "enterprise_url" TEXT,
    "bot_token" TEXT,
    "bot_id" TEXT,
    "bot_user_id" TEXT,
    "bot_scopes" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "installed_at" TIMESTAMP(3) NOT NULL,
    "user_id" TEXT,

    CONSTRAINT "SlackInstallation_pkey" PRIMARY KEY ("team_id")
);

-- CreateIndex
CREATE UNIQUE INDEX "SlackInstallation_team_id_enterprise_id_key" ON "SlackInstallation"("team_id", "enterprise_id");
