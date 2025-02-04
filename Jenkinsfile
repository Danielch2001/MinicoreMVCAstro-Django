pipeline {
    agent any

    stages {
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
                        userRemoteConfigs: [[url: 'https://github.com/Danielch2001/MinicoreMVCAstro-Django.git']]
                    ])
                }
            }
        }

        stage('Detect Backend File Paths') {
            steps {
                script {
                    def settingsPath = sh(script: "find backend -name settings.py", returnStdout: true).trim()
                    def urlsPath = sh(script: "find backend -name urls.py", returnStdout: true).trim()
                    def wsgiPath = sh(script: "find backend -name wsgi.py", returnStdout: true).trim()

                    if (settingsPath && urlsPath && wsgiPath) {
                        echo "✅ Archivos detectados correctamente:"
                        echo "settings.py encontrado en: ${settingsPath}"
                        echo "urls.py encontrado en: ${urlsPath}"
                        echo "wsgi.py encontrado en: ${wsgiPath}"
                    } else {
                        error "❌ No se encontraron uno o más archivos críticos (settings.py, urls.py, wsgi.py). Verifica la estructura del proyecto."
                    }
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
                sh 'docker-compose build frontend'
                
                echo "📂 Verificando archivos en /app después de la construcción..."
                sh 'docker-compose run --rm frontend ls -lah /app || true'
            }
        }

        stage('Run Containers') {
            steps {
                echo "🚀 Iniciando los contenedores..."
                sh 'docker-compose up -d'
                
                echo "📌 Verificando estado de los contenedores..."
                sh '''
                docker ps --format "table {{.Names}}\t{{.State}}\t{{.Ports}}"
                '''
            }
        }

        stage('Verify Backend Files') {
            steps {
                echo "🛠️ Verificando archivos en el contenedor backend..."
                
                script {
                    def backendStatus = sh(script: "docker inspect -f '{{.State.Status}}' backend", returnStdout: true).trim()
                    if (backendStatus != "running") {
                        error "❌ El contenedor backend no está en ejecución."
                    }
                }

                sh '''
                docker-compose run --rm backend ls -lah /app || true
                docker-compose run --rm backend find / -name "manage.py" || true
                docker-compose logs backend || true
                '''
            }
        }

        stage('Verify Frontend Files') {
            steps {
                echo "🛠️ Verificando archivos en el contenedor frontend..."
                
                script {
                    def frontendStatus = sh(script: "docker inspect -f '{{.State.Status}}' frontend", returnStdout: true).trim()
                    if (frontendStatus != "running") {
                        error "❌ El contenedor frontend no está en ejecución."
                    }
                }

                sh '''
                docker-compose run --rm frontend ls -lah /app || true
                docker-compose run --rm frontend find /app || true
                docker-compose logs frontend || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Ejecutando pruebas en el backend..."
                sh '''
                docker-compose run --rm backend pytest || true
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
