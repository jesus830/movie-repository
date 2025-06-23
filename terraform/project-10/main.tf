resource "aws_iam_user" "developer" {
  name = "developer-user"
}

resource "aws_iam_group" "developers" {
  name = "developers"
}

resource "aws_iam_group_membership" "developers" {
  name = "developers-membership"
  users = [aws_iam_user.developer.name]
  group = aws_iam_group.developers.name
}

resource "aws_iam_group_policy_attachment" "developers_s3" {
  group      = aws_iam_group.developers.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

resource "aws_iam_access_key" "developer" {
  user = aws_iam_user.developer.name
}

output "access_key_id" {
  value = aws_iam_access_key.developer.id
}

output "secret_access_key" {
  value     = aws_iam_access_key.developer.secret
  sensitive = true
}