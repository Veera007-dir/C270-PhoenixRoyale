pipeline {
  agent {
    docker { image 'python:3.11-slim' }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        sh '''
	  python3 --version
	  pip3 --version
          pip3 install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          pytest -q
        '''
      }
    }
  }

  post {
    success { echo 'Tests passed. Safe to proceed.' }
    failure { echo 'Tests failed. Pipeline stopped.' }
  }
}
