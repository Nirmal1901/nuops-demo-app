pipeline {
    agent any
    
    environment {
        SONAR_HOST_URL = 'http://localhost:9000'
        SONAR_TOKEN = credentials('sonar-token')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "📦 Checked out"
            }
        }
        
        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m pip install --user pytest pytest-cov
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m pytest tests/ -v --junitxml=test-results.xml --cov=. --cov-report=xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('SonarQube Analysis') {
            // Run SonarQube even if tests fail
            steps {
                script {
                    withSonarQubeEnv('SonarQube-Local') {
                        sh '''
                            sonar-scanner \
                                -Dsonar.projectKey=nuops-demo-app \
                                -Dsonar.projectName="NuOps Demo App" \
                                -Dsonar.sources=. \
                                -Dsonar.exclusions=**/tests/** \
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
                    waitForQualityGate abortPipeline: false  // Don't abort, just report
                }
            }
        }
    }
    
    post {
        always {
            // Always send results to NuOps
            script {
                def qualityGate = currentBuild.result
                sh """
                    curl -X POST http://localhost:5001/webhook \
                    -H "Content-Type: application/json" \
                    -d '{
                        "job_name": "${JOB_NAME}",
                        "build_number": ${BUILD_NUMBER},
                        "status": "${currentBuild.result}",
                        "repo": "${GIT_URL}",
                        "branch": "${GIT_BRANCH}",
                        "sonar_host": "${SONAR_HOST_URL}"
                    }' || true
                """
            }
        }
    }
}
