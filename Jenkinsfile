pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "building..."
                create_venv "env"
                run_in_venv "env" "pip install --upgrade pip"
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
     virtualenv=${name}
}



def run_in_venv(String environment, String script) {
    bash: script "source ${environment}/bin/activate &&"
    bash: script script
}

