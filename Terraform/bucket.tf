#create a s3 bucket

resource "aws_s3_bucket" "weather-bucket" {
  bucket = "victor-job-2025"

  tags = {
    Name        = "weather-bucket"
    Environment = "Production"
  }
}