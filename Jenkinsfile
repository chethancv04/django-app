pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'chethancv28/django-app:latest'
        KUBECONFIG = 'C:\\Users\\chethan\\.kube\\config'
        ANSIBLE_DIR = 'D:\\Farm_ibm\\Farm-Product-E-Commerce\\ansible'  // Full path to your Ansible directory
        ANSIBLE_INVENTORY = 'D:\\Farm_ibm\\Farm-Product-E-Commerce\\ansible\\inventory.yml'  // Full path to your inventory file
        ANSIBLE_PLAYBOOK = 'D:\\Farm_ibm\\Farm-Product-E-Commerce\\ansible\\playbook.yml'  // Full path to your playbook file
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/chethancv04/django-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                    bat 'docker push %DOCKER_IMAGE%'
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python tests.py'
            }
        }

        // Add Ansible Configuration Management Stage
        stage('Configure with Ansible') {
            steps {
                script {
                    // Run the Ansible playbook to apply configuration
                    bat 'ansible-playbook -i %ANSIBLE_INVENTORY% %ANSIBLE_PLAYBOOK% --ask-become-pass'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get service django-service'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
