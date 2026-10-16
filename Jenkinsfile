pipeline {
    agent any
    stages {
        stage("Check Python") {
            steps {
                    bat '''
                        where py
                        py --version
                    '''
            }
        }

        stage("Create Virtual environment") {
            steps {
                    bat '''
                        py -3 -m venv .jenkins-venv
                    '''
            }
        }
        stage("Install dependencies") {
            steps {
                    bat '''
                        .jenkins-venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    '''
            }
        }
        stage("Run Pytest") {
            steps{
                    bat '''
                        .jenkins-venv\\Scripts\\python.exe -m pytest -v -s --junitxml=reports\\junit.xml
                    '''
            }
        }
    }
    post {
        always {
                junit testResults: 'reports/junit.xml', allowEmptyResults: true
        }
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}