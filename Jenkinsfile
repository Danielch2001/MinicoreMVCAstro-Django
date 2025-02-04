pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[url: 'https://github.com/Danielch2001/MinicoreMVCAstro-Django.git']]
                    ])
                }
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker-compose build backend'
                sh 'docker-compose run --rm backend ls -l /app'
            }
        }

        stage('Build Frontend') {
            steps {
                sh 'docker-compose build frontend'
                sh 'docker-compose run --rm frontend ls -l /app'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
                sh 'docker-compose ps'
            }
        }

        stage('Verify Backend Files') {
            steps {
                sh 'docker-compose exec backend ls -lah /app || true'
                sh 'docker-compose exec backend find /app || true'
            }
        }

        stage('Verify Frontend Files') {
            steps {
                sh 'docker-compose exec frontend ls -lah /app || true'
                sh 'docker-compose exec frontend find /app || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose exec backend pytest || true'
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
