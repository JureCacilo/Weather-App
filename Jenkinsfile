pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building..."
                bat script: "python -m venv env"
                echo "Path ${env.PATH}"
                bat script: "${workspace}/env/Scripts/python.exe -m pip install --upgrade pip"
                bat script: "${workspace}/env/Scripts/python.exe -m pip install -r requirements.txt"
            }
        }
        stage('Scan repository') {
            steps {
                echo "Scanning"
                bat script: "${workspace}/env/Scripts/python.exe branch_activity_report.py --gitea_url https://api.github.com --owner jureCacilo --repository Weather-App --days 10"
                echo "-----------------------------------------------------------------------------------------------------------"
            }
        }

        stage('Test') {
            steps {
                echo "Testing ..."
                bat script: "${workspace}/env/Scripts/python.exe -m pytest"
            }
        }

        stage('Lint') {
            steps {
                echo "Linting ...."
                bat script: "${workspace}/env/Scripts/python.exe -m pylint ${workspace}/src/JureCacilo_weather_app/controller || exit 0"

            }
        }

    }
}