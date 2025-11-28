# AgriSure Backend (Prototype)

This repository is a production-oriented backend scaffold for the AgriSure financial risk-assessment platform.
It includes a FastAPI app, Postgres models + Alembic migrations, Celery background tasks, integration stubs for
Perfios & OneVigil, S3-style storage support, Docker + docker-compose, Terraform config for AWS resources, and
a GitHub Actions workflow for CI/CD.

IMPORTANT: The Perfios and OneVigil integrations are implemented as HTTP clients with placeholders — replace
endpoints, request signing, and secret management with your actual credentials and secure storage before production.

---

## Features

- FastAPI REST API with JWT authentication  
- PostgreSQL using SQLAlchemy ORM + Alembic migrations  
- Celery + Redis for async background task processing  
- Perfios + OneVigil integration stubs  
- S3-style file storage (Boto3)  
- Docker + docker-compose for local development  
- Terraform configs for AWS (ECR, S3, Secrets Manager)  
- GitHub Actions workflow for CI → build → push to ECR  

---

## Project Structure

agrisure-backend/
│
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── celery_app.py
│   ├── deps.py
│   ├── tasks.py
│   ├── perfios_client.py
│   ├── onevigil_client.py
│   ├── storage.py
│   ├── routers/
│       ├── auth.py
│       ├── farmers.py
│       ├── consents.py
│       ├── applications.py
│       ├── bankstatements.py
│
├── alembic/
│   ├── alembic.ini
│   ├── env.py
│   ├── versions/
│       └── 0001_initial.py
│
├── terraform/
│   ├── main.tf
│   ├── ecr.tf
│   ├── s3.tf
│   ├── secretsmanager.tf
│   ├── variables.tf
│
└── .github/
    └── workflows/
        └── ci-cd.yml

---

## Environment Variables

Create a `.env` file with:

DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/agrisure  
REDIS_URL=redis://redis:6379/0  
SECRET_KEY=supersecretjwtkey  
ACCESS_TOKEN_EXPIRE_MINUTES=60  

AWS_REGION=us-east-1  
S3_BUCKET=agrisure-dev-bucket  

PERFIOS_API_URL=https://perfios.example/api  
PERFIOS_API_KEY=perfios-key-placeholder  

ONEVIGIL_API_URL=https://onevigil.example/api  
ONEVIGIL_API_KEY=onevigil-key-placeholder  

---

## Running Locally (without Docker)

Install dependencies:

pip install -r requirements.txt

Start the API server:

uvicorn app.main:app --reload

Start Celery worker:

celery -A app.celery_app.celery worker --loglevel=info

---

## Running with Docker

docker-compose up --build

API available at:

http://localhost:8000

---

## Database Migrations (Alembic)

Apply migrations:

alembic upgrade head

Create a new migration:

alembic revision --autogenerate -m "message"

---

## API Documentation

Swagger UI:

http://localhost:8000/docs

---

## ☁️ Deployment Using Terraform

cd terraform  
terraform init  
terraform apply  

Creates:

- AWS ECR repository  
- AWS S3 bucket  
- AWS Secrets Manager entries  

---

## CI/CD (GitHub Actions)

Workflow: `.github/workflows/ci-cd.yml`

It will:

- Build Docker image  
- Authenticate to AWS  
- Push the image to ECR  

---

## Notes

- Perfios + OneVigil clients are mock implementations — replace with real API logic  
- Never commit real credentials — use AWS Secrets Manager  
- This project is fully runnable for local development  

