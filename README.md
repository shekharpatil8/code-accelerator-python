# 🦩 {{microServiceName}}

> A fast, lightweight, and modern Python microservice built with FastAPI, Poetry, and Uvicorn, ideal for scalable RESTful services.

---

## 📌 Index

* [Prerequisites](#prerequisites)
* [Environment Setup](#environment-setup)
* [Run the Application](#run-the-application)
* [Run with Docker](#run-with-docker)
* [Run Tests](#run-tests)
* [Push Project to GitHub](#push-project-to-github)
* [Integrate with CircleCI](#integrate-with-circleci)

  * [1. Add Project to CircleCI](#1-add-project-to-circleci)
  * [2. Configure Environment Variables](#2-configure-environment-variables)
  * [3. Update CircleCI Config](#3-update-circleci-config)
  * [4. Commit & Trigger Build](#4-commit--trigger-build)
  * [5. Verify Build Status](#5-verify-build-status)
  * [6. View Build Artifacts](#6-view-build-artifacts)
* [Verify ECS Deployment](#verify-ecs-deployment)

---

## ✅ Prerequisites

Ensure your system has the following installed:

1. **Python** (version as defined in `pyproject.toml`)
2. **Poetry** (for dependency management)

---

## ⚙️ Environment Setup

### 1. Create a Virtual Environment:

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment:

* **Windows:**

```bash
.\.venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source .venv/Scripts/activate
```

### 3. Install Poetry:

```bash
pip install poetry
```

### 4. Install Dependencies:

```bash
poetry install --no-root
```

---

## 🚀 Run the Application

Start the server with:

```bash
PYTHONPATH=src uvicorn main:app --host 0.0.0.0 --port 8080
```

Access API documentation:

* [http://localhost:8080/docs](http://localhost:8080/docs)

---

## 🐳 Run with Docker

### 1. Build the Docker Image:

```bash
docker build -f deployments/Dockerfile -t <image:tag_name> .
```

### 2. Run the Container:

```bash
docker run -p 9001:9001 <image:tag_name>
```

The server will now be accessible at:

* [http://localhost:9001](http://localhost:9001)

---

## 🧪 Run Tests

```bash
PYTHONPATH=./:src pytest
```

Make sure the virtual environment is activated before running tests.

---

## 🗂️ Push Project to GitHub

### 1. Create a GitHub Repository

* Go to [https://github.com](https://github.com) and create a new repository.

### 2. Clone the Repository Locally

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 3. Copy Project Files into the Repo

```bash
cp -r /path/to/your/project/* .
```

### 4. Initial Commit

```bash
git add .
git commit -m "initial commit"
```

### 5. Push to GitHub

```bash
git push origin main
```

---

## ♻️ Integrate with CircleCI

### 1. Add Project to CircleCI

1. Visit [https://circleci.com](https://circleci.com)
2. Log in with GitHub
3. Click **"Add Project"**
4. Find your repository and click **"Set Up Project"**
5. Choose `.circleci/config.yml` as the configuration path

### 2. Configure Environment Variables

* Navigate to **Project Settings > Environment Variables** in CircleCI
* Add the following:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_DEFAULT_REGION` (e.g., `ap-south-1`)
  * `AWS_ACCOUNT_ID`

### 3. Update CircleCI Config

Ensure `.circleci/config.yml` is updated with actual values replacing placeholders like `CHANGE_ME`.

### 4. Commit & Trigger Build

```bash
git add .circleci/config.yml
git commit -m "Add CircleCI pipeline for Python service"
git push origin <branch_name>
```

### 5. Verify Build Status

* Open CircleCI Dashboard
* Select your project
* View logs of each job (install, test, build, deploy)

### 6. View Build Artifacts

* In the CircleCI job screen, go to **Artifacts** tab
* Check uploaded test reports or deployment logs

---

## 🔍 Verify ECS Deployment

After your service is deployed to ECS, follow the steps below to verify the deployment using the provided endpoints.

### ✅ Steps to Follow:

1. Log in to the **[AWS ECS Console](https://console.aws.amazon.com/ecs/)**.
2. Navigate to your ECS **Service** and find the **Application Load Balancer (ALB) DNS name**.
3. Replace `<ALB_DNS_NAME>` and `<service_name>` in the URLs below to access your deployed endpoints.

---

### 🔗 **Verification Endpoints**

* **Swagger UI**
  Access the interactive API documentation here:

  ```
  https://<ALB_DNS_NAME>/<service_name>/docs

If all goes well, the FastAPI Swagger UI will appear live from ECS! 🎉

---
