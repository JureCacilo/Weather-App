pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "building..."
                bat script: "python -c \"print('Deluje')\""
            }
        stage('Test') {
            steps {
                echo "Testing"
            }
        }
        }
    }
}

