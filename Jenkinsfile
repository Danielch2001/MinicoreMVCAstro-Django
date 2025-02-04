pipeline {
    agent any

    environment {
        BACKEND_IMAGE = 'backend'
        FRONTEND_IMAGE = 'frontend'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Danielch2001/MinicoreMVCAstro-Django.git'
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker-compose build backend'
            }
        }

        stage('Build Frontend') {
            steps {
                sh 'docker-compose build frontend'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker exec backend pytest'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker system prune -f'
            }
        }
    }

    post {
        always {
            sh 'docker-compose logs'
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Deployment successful!'
        }
    }
}
