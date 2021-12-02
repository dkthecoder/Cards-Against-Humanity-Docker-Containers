pipeline {
    agent any

    // add timestamps to the console log
    options {
        timestamps()
    }

    environment {
        DOCKER_UNAME = credentials('docker_uname')
        DOCKER_PWORD = credentials('docker_pword')
    }

    stages {

        stage('update/upgrade packages') {
            steps {
                sh "sudo apt update"
                sh "sudo apt upgrade"
            }
        }

        //stage('clone repo') {
            //steps {
                //sh "echo 'clonning repo' "
                // change dir
                //sh "cd /" 
                // Clone repo.
                //sh "git clone https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers.git"
                //sh "echo 'COMPLETED repo clone' "
            //}
        //}


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

        stage('Config and deploy') {
            steps {
                sh "scp docker-compose.yaml jenkins-vm:/home/jenkins/docker-compose.yaml"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
    }

    //post {
        //always {
            //junit '**/*.xml'
            //cobertura coberturaReportFile: 'frontend/coverage.xml', failNoReports: false
            //cobertura coberturaReportFile: 'blackcards/coverage.xml', failNoReports: false
            //cobertura coberturaReportFile: 'whitecards/coverage.xml', failNoReports: false
            //cobertura coberturaReportFile: 'magicmaker/coverage.xml', failNoReports: false
            //sh "docker-compose down || true"
        //}
    //}
}