pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'chethancv28/django-app:latest'  // Update with your actual Docker Hub image
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/chethancv04/django-app.git' // Replace with your actual GitHub repo URL
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials']) {
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods'
                sh 'kubectl get service django-service'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
