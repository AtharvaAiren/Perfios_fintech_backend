resource "aws_s3_bucket" "storage" {
  bucket = var.s3_bucket
  acl    = "private"
  versioning {
    enabled = true
  }
}
