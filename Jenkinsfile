pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/Danielch2001/MinicoreMVCAstro-Django.git'
        GIT_CREDENTIALS_ID = 'github-credentials'
    }

    stages {
        stage('Pre-Build: Análisis Estático y Dependencias') {
            steps {
                echo "🔍 Analizando código..."
                sh '''
                pip install --user flake8 pylint pytest || true
                npm install -g eslint || true
                flake8 backend/ || true
                pylint backend/ || true
                eslint frontend/ || true
                npm audit || true
                '''
            }
        }

        stage('Cleanup Previous Containers') {
            steps {
                echo "🧹 Eliminando contenedores y volúmenes antiguos..."
                sh '''
                docker-compose down --volumes --remove-orphans || true
                docker system prune -f || true
                '''
            }
        }

        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[url: GIT_REPO, credentialsId: GIT_CREDENTIALS_ID]]
                    ]])
                }
            }
        }

        stage('Build Backend') {
            steps {
                echo "🚀 Construyendo el backend..."
                sh 'docker-compose build backend'
                echo "📂 Verificando archivos en /app después de la construcción..."
                sh 'docker-compose run --rm backend ls -lah /app || true'
            }
        }

        stage('Build Frontend') {
            steps {
                echo "🚀 Construyendo el frontend..."
                sh '''
                docker-compose build frontend
                docker-compose run --rm frontend npm install
                '''
                echo "📂 Verificando archivos en /app después de la construcción..."
                sh 'docker-compose run --rm frontend ls -lah /app || true'
            }
        }

        stage('Run Containers') {
            steps {
                echo "🚀 Iniciando los contenedores..."
                sh 'docker-compose up -d'
                
                echo "📌 Verificando estado de los contenedores..."
                sh 'docker ps --format "table {{.Names}}\t{{.State}}\t{{.Ports}}"'
            }
        }

        stage('Run Backend Tests') {
            steps {
                echo "🧪 Ejecutando pruebas en el backend..."
                sh '''
                docker-compose run --rm backend pytest || true
                '''
            }
        }

        stage('Run Frontend Tests') {
            steps {
                echo "🧪 Ejecutando pruebas en el frontend..."
                sh '''
                docker-compose run --rm frontend npm test || true
                '''
            }
        }

        stage('Push to GitHub') {
            steps {
                echo "🚀 Subiendo cambios a GitHub para que Railway los despliegue..."
                sh '''
                git config --global user.email "tu-email@example.com"
                git config --global user.name "Jenkins CI"
                git add .
                
                if git diff --quiet && git diff --staged --quiet; then
                    echo "⚠️ No hay cambios detectados, enviando un commit vacío..."
                    git commit --allow-empty -m "🚀 Auto-deploy desde Jenkins (sin cambios)"
                else
                    git commit -m "🚀 Auto-deploy desde Jenkins"
                fi

                git push https://${GIT_CREDENTIALS_ID}@github.com/Danielch2001/MinicoreMVCAstro-Django.git HEAD:main
                '''
            }
        }        
    }

    post {
        failure {
            echo '❌ Build failed! Limpiando posibles residuos...'
            sh '''
            docker-compose down --volumes --remove-orphans || true
            docker system prune -f || true
            '''
            sh 'docker-compose logs'
        }
    }
}
