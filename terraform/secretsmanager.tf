resource "aws_secretsmanager_secret" "app_secrets" {
  name = "${var.ecr_repo_name}-secrets"
  description = "Secrets for AgriSure backend"
}

resource "aws_secretsmanager_secret_version" "app_secrets_version" {
  secret_id     = aws_secretsmanager_secret.app_secrets.id
  secret_string = jsonencode({
    DATABASE_URL = var.database_url
    SECRET_KEY = var.secret_key
    PERFIOS_API_KEY = var.perfios_api_key
    ONEVIGIL_API_KEY = var.onevigil_api_key
  })
}
