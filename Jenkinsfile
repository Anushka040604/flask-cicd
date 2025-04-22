pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'flask-cicd-demo'
        K8S_DEPLOYMENT_DIR = 'k8s'  // Folder containing deployment.yaml and service.yaml
        DEPLOYMENT_FILE = "${K8S_DEPLOYMENT_DIR}/deployment.yaml"
        SERVICE_FILE = "${K8S_DEPLOYMENT_DIR}/service.yaml"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Check out the code from GitHub
                    git branch: 'main', url: 'https://github.com/Anushka040604/flask-cicd-demo.git'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Set up the Python virtual environment and run the tests
                    bat '''
                        echo Setting up Python virtual environment...
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    bat 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Push Docker Image') {
            when {
                expression { return currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    // Push Docker image to Docker registry
                    bat 'docker push ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            when {
                expression { return currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    // Deploy to Kubernetes using both deployment.yaml and service.yaml
                    bat "kubectl apply -f ${DEPLOYMENT_FILE}"
                    bat "kubectl apply -f ${SERVICE_FILE}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Something went wrong! Please check the logs.'
        }
    }
}
