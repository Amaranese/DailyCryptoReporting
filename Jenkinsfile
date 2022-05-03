pipeline {
    agent any

    triggers {
        //pollSCM('*/5 * * * 1-5')
        cron('0 * * * *')
    }
    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }
    environment {
      PATH="/users/shared/jenkins/miniconda3/bin:$PATH"
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Build environment') {
            steps {
                sh '''conda create --yes -n ${BUILD_TAG} python
                      source activate ${BUILD_TAG} 
                      pip install -r requirements.txt
                    '''
            }
        }
        stage('Test environment & pull metrics') {
            steps {
                sh '''source activate ${BUILD_TAG} 
                      pip list
                      which pip
                      which python
                      python3 gbpReport.py
                    '''
            }
        }
        stage('Generate Reports') {
            steps {
                build 'BASEGBP-REPORT'
            }
        }
        stage('Static code metrics') {
            steps {
                echo "Raw metrics"
                sh  ''' source activate ${BUILD_TAG}
                        radon raw --json testTargets/ > /Users/adammcmurchie/projects/Jenkins-Stuff/coinmarketcap/raw_report.json
                        radon cc --json testTargets/ > /Users/adammcmurchie/projects/Jenkins-Stuff/coinmarketcap/cc_report.json
                        radon mi --json testTargets/ > /Users/adammcmurchie/projects/Jenkins-Stuff/coinmarketcap/mi_report.json
                    '''
            }
        }
    }
    post {
        always {
            sh 'conda remove --yes -n ${BUILD_TAG} --all'
        }
        success {  
             echo "build ${BUILD_TAG} succesfull" 
         }  
         failure {  
             mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "murchie@gmail.com";  
         }


    }
}