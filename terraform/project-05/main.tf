resource "aws_lambda_function" "hello" {
  filename         = "hello.zip"
  function_name    = "hello-world"
  role            = aws_iam_role.lambda.arn
  handler         = "index.handler"
  runtime         = "python3.9"
}

resource "aws_iam_role" "lambda" {
  name = "lambda-role"
  
  assume_role_policy = jsonencode({
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  output_path = "hello.zip"
  source {
    content  = "def handler(event, context): return {'statusCode': 200, 'body': 'Hello World!'}"
    filename = "index.py"
  }
}

output "function_name" {
  value = aws_lambda_function.hello.function_name
}