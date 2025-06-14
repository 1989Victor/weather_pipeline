**API to S3 Data Pipeline with Airflow and Terraform**


**Overview**

This project implements a fully automated data pipeline that fetches data from a public API (weather API) on a daily basis and stores it in Amazon S3. 
The infrastructure is provisioned using Terraform, while the workflow is managed and scheduled via Apache Airflow.


**Tech Stack**

Python

Apache Airflow – Workflow orchestration

Terraform – Infrastructure as code

AWS S3 – Storage layer

AWS IAM – Access control

AWS Systems Manager (SSM) – Secure credentials storage




**Pipeline Architecture**

Daily API Extraction

A scheduled Airflow DAG sends requests to an external API and retrieves data.

**Data Storage in S3**

Extracted data is written to a dedicated S3 bucket in Parquet format.
Only write permissions are granted to the Airflow user (no read access for security).

**Secure Credential Management**

API keys and AWS credentials are stored as SSM parameters (AWS Systems Manager) and injected securely into the Airflow environment.


**Infrastructure Setup (via Terraform)**

**S3 Bucket**

A uniquely named bucket is provisioned to store pipeline outputs.

**IAM Policy/User**

A minimal-permission IAM user is created for Airflow.

Permissions are restricted to write-only access to the S3 bucket.

**SSM Parameters**

AWS credentials (Access Key and Secret Key) are stored as secure parameters in SSM.
Airflow accesses these parameters dynamically during runtime.

**Airflow Orchestration**

Airflow is used to:

Trigger the pipeline on a daily schedule

Handle failures with retries

Pull credentials securely from SSM

Call the API, process data, and push to S3.
