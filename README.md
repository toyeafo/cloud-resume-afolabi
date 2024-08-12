# Cloud Resume Project

## Overview

This project is a cloud-hosted resume application that leverages modern cloud technologies to provide a highly available and scalable personal website. The application includes both frontend and backend components, with the backend being powered by AWS Lambda and managed through Terraform, and the frontend hosted as a static website. The project also incorporates CI/CD pipelines using GitHub Actions to automate testing and deployment.

## Features

- **Cloud-Hosted**: The resume is hosted on the cloud, ensuring high availability and scalability.
- **Serverless Backend**: Utilizes AWS Lambda for backend functionality, making the application cost-efficient and easily maintainable.
- **Infrastructure as Code**: Managed using Terraform, allowing for consistent and repeatable deployments.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Automated pipelines using GitHub Actions for testing and deploying the application.
- **Responsive Frontend**: A modern, responsive design for the resume, ensuring it looks great on all devices.

## Requirements

- AWS account (for deploying the backend and hosting the frontend)
- Terraform (for infrastructure management)
- Python 3.x (for Lambda function and testing)
- GitHub account (for CI/CD integration)

## Installation

### Backend Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/cloud-resume.git
    cd cloud-resume/backend-code
    ```

2. **Configure AWS Credentials**:
   
   Ensure your AWS CLI is configured with the necessary credentials to deploy resources.

    ```bash
    aws configure
    ```

3. **Deploy Infrastructure**:
   
   Use Terraform to provision the necessary AWS resources, including the Lambda function and any supporting services.

    ```bash
    terraform init
    terraform apply
    ```

4. **Deploy Lambda Function**:
   
   Deploy the Lambda function defined in `lambda_function.py`.

    ```bash
    zip function.zip lambda_function.py
    aws lambda update-function-code --function-name <YourLambdaFunctionName> --zip-file fileb://function.zip
    ```

### Frontend Setup

1. **Navigate to the Frontend Directory**:

    ```bash
    cd ../frontend-code
    ```

2. **Deploy Frontend**:

   The frontend can be hosted on services like AWS S3 (as a static website), or using GitHub Pages.

   For AWS S3:

    ```bash
    aws s3 cp . s3://your-s3-bucket-name --recursive
    ```

3. **Update DNS Settings** (Optional):

   If using a custom domain, update your DNS settings to point to the S3 bucket or other hosting service.

### CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/push-frontend.yaml`) that automates the deployment process upon pushing changes to the repository.

## Project Structure

- **`.github/workflows/push-frontend.yaml`**: GitHub Actions workflow for CI/CD.
- **`backend-code/`**: Contains backend-related code, including AWS Lambda function and Terraform configurations.
  - **`lambda_function.py`**: Python script for the AWS Lambda function.
  - **`main.tf`**: Terraform configuration for deploying AWS resources.
  - **`test_lambda_handler.py`**: Test file for the Lambda function.
- **`frontend-code/`**: Contains frontend-related files.
  - **`index.html`**: Main HTML file for the resume.
  - **`js/index.js`**: JavaScript file for frontend logic.
  - **`styles/`**: CSS files for styling the frontend.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **`README.md`**: Documentation file for the project (this file).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
