pipeline {
    agent any
    stages {
        stage("Check Python") {
            steps {
                dir('C:/Projects/traffic_shaping') {
                    bat '''
                        where py
                        py --version
                    '''
                }
            }
        }

        stage("Create Virtual environment") {
            steps {
                dir('C:/Projects/traffic_shaping') {
                    bat '''
                        py -3 -m venv .jenkins-venv
                    '''
                }
            }
        }
        stage("Install dependencies") {
            steps {
                dir('C:/Projects/traffic_shaping') {
                    bat '''
                        .jenkins-venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    '''
                }
            }
        }
        stage("Run Pytest") {
            steps{
                dir("C:/Projects/traffic_shaping") {
                    bat '''
                        .jenkins-venv\\Scripts\\python.exe -m pytest -v -s --junitxml=reports\\junit.xml
                    '''
                }
            }
        }
    }
    post {
        always {
            dir('C:/Projects/traffic_shaping') {
                junit testResults: 'reports/junit.xml', allowEmptyResults: true
            }
        }
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}