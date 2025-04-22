pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
               git branch: 'main', url: 'https://github.com/Anushka040604/flask-cicd-demo.git'
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-cicd-demo .'
            }
        }
        stage('Push Docker Image') {
            when {
                expression { return currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                bat 'docker push flask-cicd-demo'
            }
        }
        stage('Deploy to Kubernetes') {
            when {
                expression { return currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                bat 'kubectl apply -f k8s.yaml'
            }
        }
    }
    post {
        failure {
            echo 'Something went wrong!'
        }
    }
}
