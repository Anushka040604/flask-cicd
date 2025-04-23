# Flask App with CI/CD on GCP Kubernetes using GitHub Actions

This project demonstrates a complete CI/CD pipeline for a Flask application using **GitHub Actions** and **GCP Kubernetes (GKE)**. The pipeline builds Docker images, runs tests, and deploys the application automatically on code changes.

---

## 🚀 Tech Stack

- **Flask** – Python web framework
- **Docker** – Containerization
- **Kubernetes (GKE)** – Container orchestration
- **GitHub Actions** – CI/CD automation
- **Google Cloud Platform (GCP)** – Deployment platform

---

## 🛠️ Features of the CI/CD Pipeline

- Automatically **triggers on push to `main`**
- Installs dependencies and **runs tests** using `pytest`
- Builds a **Docker image** and pushes to **Docker Hub**
- Deploys the app to **Google Kubernetes Engine (GKE)**
- Checks rollout status and logs pod output

---

## 📦 Folder Structure

├── app/ # Flask app code ├── Dockerfile # Docker build instructions ├── requirements.txt # Python dependencies ├── deployment.yaml # Kubernetes Deployment manifest ├── service.yaml # Kubernetes Service manifest └── .github/workflows/ └── ci-cd.yml # GitHub Actions workflow


---

## 🔐 GitHub Secrets Required

Go to your repository → **Settings → Secrets → Actions**, and add the following:

| Secret Name         | Description                           |
|---------------------|---------------------------------------|
| `DOCKER_USERNAME`   | Docker Hub username                   |
| `DOCKER_PASSWORD`   | Docker Hub password                   |
| `KUBECONFIG`        | Base64-encoded Kubernetes config file |

Generate `KUBECONFIG` (in PowerShell, replace `base64` with `certutil`):
```bash
cat ~/.kube/config | base64

