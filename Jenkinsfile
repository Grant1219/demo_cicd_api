pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                sh 'echo "testing tuxinator_api..."'
                withPythonEnv('python') {
                    pysh 'python setup.py test'
                }
            }
            post {
                success {
                    sh 'echo "testing succeeded"'
                }
            }
        }
        stage('Build') {
            steps {
                sh 'echo "building tuxinator_api..."'
                withPythonEnv('python') {
                    pysh 'python setup.py build'
                }
            }
            post {
                success {
                    sh 'echo "building succeeded"'
                    withPythonEnv('python') {
                        pysh 'python setup.py sdist upload'
                    }
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
            }
        }
    }
}
