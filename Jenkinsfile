pipeline {
    agent any
    
    environment {
        SONAR_HOST_URL = 'http://sonarqube:9000'
        SONAR_TOKEN = credentials('sonar-token')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "📦 Checked out from ${env.GIT_BRANCH}"
            }
        }
        
        stage('Setup Python') {
            steps {
                sh '''
                    echo "🐍 Setting up Python environment..."
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    echo "🧪 Running unit tests..."
                    python3 -m pytest tests/ -v --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                    publishHTML([
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQube-Local') {
                        sh '''
                            echo "🔍 Running SonarQube analysis..."
                            sonar-scanner \
                                -Dsonar.projectKey=nuops-demo-app \
                                -Dsonar.projectName="NuOps Demo App" \
                                -Dsonar.projectVersion=1.0 \
                                -Dsonar.sources=. \
                                -Dsonar.exclusions=**/tests/**,**/venv/** \
                                -Dsonar.python.coverage.reportPaths=coverage.xml \
                                -Dsonar.python.xunit.reportPath=test-results.xml
                        '''
                    }
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
    
    post {
        success {
            echo "✅ Pipeline succeeded! All tests passed and quality gate is green."
        }
        failure {
            echo "❌ Pipeline failed! Check the logs above."
            
            // Trigger NuOps webhook for auto-remediation
            sh '''
                curl -X POST http://host.docker.internal:5001/webhook \
                -H "Content-Type: application/json" \
                -d '{
                    "job_name": "'${JOB_NAME}'",
                    "build_number": '${BUILD_NUMBER}',
                    "status": "FAILED",
                    "repo": "'${GIT_URL}'",
                    "branch": "'${GIT_BRANCH}'"
                }' || true
            '''
        }
    }
}
