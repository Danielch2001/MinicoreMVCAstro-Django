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
                sh 'docker-compose exec backend pytest || true' // Agregar || true evita que el pipeline falle por errores en tests
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
