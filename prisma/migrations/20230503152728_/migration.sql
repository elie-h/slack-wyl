/*
  Warnings:

  - You are about to drop the column `bot_scopes` on the `SlackInstallation` table. All the data in the column will be lost.
  - You are about to drop the `Post` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `User` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "Post" DROP CONSTRAINT "Post_author_id_fkey";

-- AlterTable
ALTER TABLE "SlackInstallation" DROP COLUMN "bot_scopes";

-- DropTable
DROP TABLE "Post";

-- DropTable
DROP TABLE "User";

-- CreateIndex
CREATE INDEX "SlackInstallation_team_id_idx" ON "SlackInstallation"("team_id");

-- CreateIndex
CREATE INDEX "SlackInstallation_team_id_enterprise_id_idx" ON "SlackInstallation"("team_id", "enterprise_id");
