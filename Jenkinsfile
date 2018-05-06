pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "building tuxinator_api..."'
                sh 'python setup.py sdist'
            }
            post {
                success {
                    sh 'echo "build succeeded"'
                    archiveArtifacts artifacts: dist/*, fingerprint: true
                }
            }
        }
    }
}
