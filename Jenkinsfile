def git_tag = null
pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = credentials("1177a959-db47-4665-8105-e050514cbe1a")
    }

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
        stage("Debug") {
            steps {
            while (true) {
                def cmd = input message: 'What to run:', parameters: [string(defaultValue: '', description: '', name: 'cmd')]
                try {
                    print Eval.x(this,cmd)
                } catch (e) {
                print e
                }
            }
        }

        stage('Scan repository') {
            steps {
                echo "Scanning..."
                bat script: "${workspace}/env/Scripts/python.exe branch_activity_report.py --github_url https://api.github.com --token ${GITHUB_CREDENTIALS_PSW} --owner ${GITHUB_CREDENTIALS_USR} --repository Weather-App --days 10"
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
                bat script: "${workspace}/env/Scripts/python.exe -m pylint ${workspace}/src/ || exit 0"

            }
        }

        stage('Deploy if taged') {
            when {
                expression {
                    return git_tag;
                }
            }
            steps {
                echo "Packaging ..."
                bat script: "${workspace}/env/Scripts/python.exe -m pip install wheel"
                bat script: "${workspace}/env/Scripts/python.exe setup.py sdist bdist_wheel"
                echo "Publish to TestPyPi...."
            }
        }
    }
}
