# AI-Powered GitHub Pull Request Reviewer

An AI-powered code review application that analyzes GitHub pull requests, identifies potential code issues, and provides actionable suggestions to improve code quality.

## 🚀 Project Overview

The goal of this project is to automate parts of the code review process using AI and static code analysis.

When a developer creates a pull request, the application will analyze the changed code, identify potential bugs and security issues, and provide suggestions for improvement.

## 🛠️ Tech Stack

**Backend**
- Python
- FastAPI
- SQLAlchemy
- Pydantic

**Database**
- PostgreSQL

**Tools**
- Git and GitHub
- Swagger UI
- Uvicorn

**Planned Technologies**
- GitHub API and Webhooks
- Large Language Models (LLMs)
- React
- Docker
- Pytest

## ✨ Planned Features

- [x] FastAPI backend setup
- [x] PostgreSQL database integration
- [x] SQLAlchemy database models
- [x] CRUD operations for review requests
- [x] Database credential configuration using environment variables
- [ ] GitHub OAuth integration
- [ ] GitHub webhook integration
- [ ] Pull request diff extraction
- [ ] AI-powered code analysis
- [ ] Automated review comments on GitHub
- [ ] React dashboard
- [ ] Automated testing and deployment

## 📁 Project Structure

```text
ai-powered-github-pr-reviewer/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── .env
├── .gitignore
└── README.md
```

Note: `.env` is a local configuration file and should not be committed to GitHub.

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/sejalalle/ai-powered-github-pr-reviewer.git
cd ai-powered-github-pr-reviewer
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://reviewer_user:YOUR_PASSWORD@localhost:5432/ai_code_reviewer
```

Replace `YOUR_PASSWORD` with your PostgreSQL user's password.

### 5. Start the application

```bash
uvicorn app.main:app --reload
```

### 6. Explore the API

- API: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs

## 📌 Current Status

The project currently supports database-backed CRUD operations for review requests using FastAPI, SQLAlchemy and PostgreSQL.

GitHub integration and AI-powered code analysis are planned for upcoming development stages.

## 🎯 Project Objective

Build a practical AI-powered developer tool while exploring backend engineering, database management, API development, GitHub integration and AI application development.

## 👨‍💻 Author

Sejal Alle