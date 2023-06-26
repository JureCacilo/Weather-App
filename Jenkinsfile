pipeline {
    agent any
    options { skipDefaultCheckout() }
    stages {
        stage('Build') {
            steps {
                echo "building..."
                bat script: "python -m venv env"
                echo "Path ${env.PATH}"
                bat script: "${workspace}/env/Scripts/python.exe -m pip install -r requirements.txt"
                //bat: script ""
                //run_in_venv "env", "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                echo "Testing"
            }
        }
    }
}