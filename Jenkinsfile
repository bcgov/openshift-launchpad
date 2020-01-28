pipeline {
    agent any
    options {
        disableResume()
    }
    stages {
        stage('Kill any older builds') {
            steps {
                script {
                    def buildNumber = env.BUILD_NUMBER as int
                    if (buildNumber > 1) milestone(buildNumber - 1)
                    milestone(buildNumber)
                }
            }
        }
        stage('Build images') {
            steps {
                sh 'docker-compose -f docker-compose-ci.yml build --parallel'
            }
        }
        stage('Run Client Tests') {
            steps {
                sh 'docker-compose -f docker-compose-ci.yml run client npm test'
            }
        }
        stage('Run Server Tests') {
            steps {
                sh 'docker-compose -f docker-compose-ci.yml run server python manage.py test'
            }
        }
        stage('Deploy to Server') {
            when {
              environment name: 'CHANGE_TARGET', value: 'master'
            }
            steps {
                script {

                    withCredentials([file(credentialsId: 'swu-prod-env', variable: 'FILE_PATH')]) {
                        // Prepare production environment vars
                        def environment_vars = readFile "${FILE_PATH}"
                        writeFile file: 'env.prod', text: "${environment_vars}"
                    }

                    withCredentials([sshUserPrivateKey(credentialsId: 'ssh-instance-key', keyFileVariable: 'keyFile', usernameVariable: 'username')]) {
                        def remote = [:]
                        remote.name = "$AWS_INSTANCE_IP_ADDRESS"
                        remote.host = "$AWS_INSTANCE_IP_ADDRESS"
                        remote.user = username
                        remote.identityFile = keyFile
                        remote.allowAnyHosts = true

                        sshCommand remote: remote, command: "sudo rm -rf /tmp/workspace"
                        sshPut remote: remote, from: '.', into: '/tmp'
                        sshScript remote: remote, script: "deployment/scripts/deploy-application.sh"
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Running cleanup'
            sh 'docker-compose -f docker-compose-ci.yml down --rmi all --volumes || true'
            sh 'docker-compose -f docker-compose-ci.yml rm -f -v -s || true'
        }
    }
}
