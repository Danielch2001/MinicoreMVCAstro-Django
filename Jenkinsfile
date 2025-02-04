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
        echo "🛠️ Verificando archivos en el contenedor backend..."
        
        // Lista el contenido de /app para ver si manage.py está allí
        sh 'docker-compose run --rm backend ls -lah /app || true'
        
        // Busca en todo el contenedor dónde está manage.py
        sh 'docker-compose run --rm backend find / -name "manage.py" || true'

        // Si encuentra el archivo, muestra su contenido para verificarlo
        sh 'docker-compose run --rm backend find / -name "manage.py" -exec cat {} \\; || true'

        // Muestra los logs del backend
        sh 'docker-compose logs backend'
    }
}




stage('Verify Frontend Files') {
    steps {
        echo "🛠️ Verificando archivos en el contenedor frontend..."
        sh 'docker-compose exec frontend ls -lah /app || true'
        sh 'docker-compose exec frontend find /app || true'
        sh 'docker-compose exec frontend cat /app/package.json || true'
        sh 'docker-compose logs frontend'
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
