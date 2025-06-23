resource "aws_s3_bucket" "website" {
  bucket = "my-static-website-${random_id.bucket_suffix.hex}"
}

resource "aws_s3_bucket_website_configuration" "website" {
  bucket = aws_s3_bucket.website.id
  index_document {
    suffix = "index.html"
  }
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

output "website_url" {
  value = aws_s3_bucket_website_configuration.website.website_endpoint
}