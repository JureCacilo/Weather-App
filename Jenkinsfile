pipeline {
    agent any
    stages {
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

