pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "echo 'building...'"
                checkout scm
                create_venv "env"
                run_in_venv "env", "pip install --upgrade pip"
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


def create_venv(String name) {
    sh "virtualenv ${name}"
}

def run_in_venv(String environment, String script) {
    sh "source ${environment}/bin/activate && " + script
}