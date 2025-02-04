pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']], // Asegurar que sea 'main' y no 'master'
                        userRemoteConfigs: [[url: 'https://github.com/Danielch2001/MinicoreMVCAstro-Django.git']]
                    ])
                }
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
                sh 'docker-compose exec backend pytest'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker-compose down'
            }
        }
    }

    post {
        failure {
            echo 'Build failed!'
            sh 'docker-compose logs'
        }
    }
}
