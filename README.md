# MY CLOUD RESUME

Welcome to my project on deploying my resume as a dynamic web application using AWS services. In this project, I utilized various AWS services, including Amazon S3, Amazon CloudFront, Amazon Route 53, Amazon DynamoDB, Amazon API Gateway, AWS Lambda, and the Python Boto3 library, to host my resume online and collect visitor data.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Setup AWS Resources](#setup-aws-resources)
- [Deploying the Resume](#deploying-the-resume)
- [Monitoring and Analytics](#monitoring-and-analytics)

## Project Overview

For this project, I wanted to make my resume accessible as a dynamic web application. AWS services provided an excellent and scalable infrastructure to achieve this goal.

## Prerequisites

Before starting this project, I ensured that I had the following prerequisites:

- An AWS account with the necessary permissions.
- My custom domain or subdomain - https://toyeafolabi-resume.com/.
- AWS CLI and Boto3 library installed and configured on my local machine.
- Basic knowledge of HTML, CSS, and JavaScript for customizing my resume.

## Setup AWS Resources

1. **Amazon S3**:
   - I created an S3 bucket named `cloud-resume-toye`.
   - Uploaded my resume files (HTML, CSS, JS) to the S3 bucket.

2. **Amazon CloudFront**:
   - I created a CloudFront distribution to accelerate content delivery.
   - Connected it to my S3 bucket as the origin.

3. **Amazon Route 53**:
   - I created a Route 53 hosted zone.
   - Configured my domain/subdomain and pointed it to my CloudFront distribution.

4. **Amazon DynamoDB**:
   - I created a DynamoDB table to store visitor data.
   - Defined the table structure, including fields like `VisitorID`, `Timestamp`, `IPAddress`.

5. **Amazon API Gateway**:
   - I created an API to collect visitor data.
   - Defined endpoints and integrated them with AWS Lambda functions.

6. **AWS Lambda**:
   - I created Lambda functions to process API requests.
   - Used the Python Boto3 library to interact with DynamoDB for data storage.

## Deploying the Resume

1. I customized my resume's HTML, CSS, and JavaScript to suit my preferences and content.

2. I deployed my resume to the S3 bucket and ensured that it was publicly accessible.

3. I tested my resume by accessing it through the CloudFront distribution or my custom domain.

## Monitoring and Analytics

To ensure that my project is performing as expected, I set up monitoring and analytics, including:

- CloudWatch alarms for performance monitoring.
- Amazon SNS for notifications.
- AWS CloudTrail for auditing and security.
