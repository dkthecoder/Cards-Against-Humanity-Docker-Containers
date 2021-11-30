pipeline {
    agent any

    // add timestamps to the console log
    options {
        timestamps()
    }

    environment {
        // TEST_PREFIX = "test-IMAGE"
        // TEST_IMAGE = "${env.TEST_PREFIX}:${env.BUILD_NUMBER}"
        // TEST_CONTAINER = "${env.TEST_PREFIX}-${env.BUILD_NUMBER}"
        // REGISTRY_ADDRESS = "my.registry.address.com"

        // SLACK_CHANNEL = "#deployment-notifications"
        // SLACK_TEAM_DOMAIN = "MY-SLACK-TEAM"
        // SLACK_TOKEN = credentials("slack_token")
        // DEPLOY_URL = "https://deployment.example.com/"

        // COMPOSE_FILE = "docker-compose.yml"
        // REGISTRY_AUTH = credentials("docker-registry")
        // STACK_PREFIX = "my-project-stack-name"
    }

    stages {

        stage('clone repo') {
            steps {
                sh "echo 'clonning repo' "
                // change dir
                sh "cd /" 
                // Clone repo.
                sh "git clone https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers.git"
                sh "echo 'COMPLETED repo clone' "
            }

        }


        // stage('Run unit tests') {
            // steps {
                // sh "bash test.sh"
            // }
        // }

        stage('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }

            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }

        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
            }
        }
    }

    post {
        always {
            junit '**/*.xml'
            cobertura coberturaReportFile: 'front-end/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'name-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'unit-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'effect-api/coverage.xml', failNoReports: false
            sh "docker-compose down || true"
        }
    }
}