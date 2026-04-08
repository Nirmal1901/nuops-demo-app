pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "📦 Checked out code successfully"
            }
        }
        
        stage('Setup Python') {
            steps {
                sh '''
                    echo "🐍 Setting up Python..."
                    python3 --version
                    pip3 install pytest pytest-cov --user
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    echo "🧪 Running tests..."
                    python3 -m pytest tests/ -v
                '''
            }
        }
        
        stage('Complete') {
            steps {
                echo "✅ Pipeline completed!"
            }
        }
    }
    
    post {
        success {
            echo "🎉 All stages passed!"
        }
        failure {
            echo "💥 Pipeline failed!"
        }
    }
}
