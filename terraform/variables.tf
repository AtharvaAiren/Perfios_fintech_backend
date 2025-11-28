variable "aws_region" {
  type = string
  default = "us-east-1"
}

variable "ecr_repo_name" {
  type = string
  default = "agrisure-backend"
}

variable "s3_bucket" {
  type = string
  default = "agrisure-backend-storage-dev-12345"
}

variable "database_url" {
  type = string
  default = ""
}

variable "secret_key" {
  type = string
  default = ""
}

variable "perfios_api_key" {
  type = string
  default = ""
}

variable "onevigil_api_key" {
  type = string
  default = ""
}
