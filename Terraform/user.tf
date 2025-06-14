# create a user 

resource "aws_iam_user" "victor_user" {
  name = "victor-api-project"

  tags = {
    tag-key = "victor-new"
  }
}

# create an access key

resource "aws_iam_access_key" "access_key" {
  user = aws_iam_user.victor_user.name

}

# create a policy

resource "aws_iam_user_policy" "weather_policy" {
  name = "victor_policy"
  user = aws_iam_user.victor_user.name
   
# Terraform's "jsonencode" function converts a Terraform expression result to valid JSON syntax
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid = "ListAllBuckets"
        Action= [
          "s3:ListAllBuckets"
        ],
        Effect = "Allow",
        Resource = "*"
      },
      {
        Action = [
	  "s3:PutObject"
        ],
        Effect   = "Allow",
        Resource = "arn:aws:s3:::victor-job-2025/*"
    }
 ]
})
}

# ssm parameter

resource "aws_ssm_parameter" "access-key" {
  name  = "access_key"
  type  = "String"
  value = aws_iam_access_key.access_key.id
}

resource "aws_ssm_parameter" "secret-key" {
  name  = "secret_key"
  type  = "String"
  value = aws_iam_access_key.access_key.secret
}
