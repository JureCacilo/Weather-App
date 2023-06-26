pipeline {
    agent any
    options { skipDefaultCheckout() }
    stages {
        stage('Build') {
            steps {
                echo "building..."
                bat script: "python -c \"print('Deluje')\""
            }
        }
        stage('Test') {
            steps {
                echo "Testing"
            }
        }
    }
}