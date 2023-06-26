pipeline {
    agent any
    options { skipDefaultCheckout() }
    stages {
        stage('Build') {
            steps {
                echo "building..."
                bat script: "python -m venv env"
                echo "Path ${env.PATH}"
                bat script: "${workspace}/env/Scripts/python.exe -m pip install --upgrade pip"
                bat script: "${workspace}/env/Scripts/python.exe -m pip install -r requirements.txt"
            }
        }
        stage('Scan repoisotry') {
            steps {
                echo "Testing"
                bat script: "${workspace}/env/Scripts/python.exe branch_activity_report.py"
            }
        }
    }
}