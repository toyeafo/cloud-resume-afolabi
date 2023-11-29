terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-2"
}

variable "function_name" {
  description = "Name of AWS Lambda Function"
  type = string
  default = "ExampleName"
}

# output "runtime_language" {
#   description = "Name of the programming language being used"
#   value = cloud_resume_terra.function_name
# }

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "archive_file" "lambda" {
  type        = "zip"
  source_file = "lambda_function.py"
  output_path = "lambda_function_payload.zip"
}

resource "aws_lambda_function" "cloud_resume_terra" {
  filename      = "lambda_function_payload.zip"
  function_name = "myLambdaFunc"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "lambda_function.lambda_handler"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.10"
}

# DynamoDB resource
resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "sitevisitors"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "VisitId"

  attribute {
    name = "VisitId"
    type = "S"
  }

  #   attribute {
  #     name = "VisitorNumber"
  #     type = "N"
  #   }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  global_secondary_index {
    name               = "SiteVisitorsIndex"
    hash_key           = "VisitId"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "INCLUDE"
    non_key_attributes = ["VisitId"]
  }

  tags = {
    Name        = "cloud-resume-table"
    Environment = "production"
  }
}
