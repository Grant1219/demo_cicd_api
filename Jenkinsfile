pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                withPythonEnv('python') {
                    sh 'echo "building tuxinator_api..."'
                    pysh 'python setup.py sdist'
                }
            }
            post {
                success {
                    sh 'echo "build succeeded"'
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
            }
        }
    }
}
