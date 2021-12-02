pipeline {
    agent any

    // add timestamps to the console log
    options {
        timestamps()
    }

    environment {
        DOCKER_USERNAME = credentials('docker_username')
        DOCKER_PASSWORD = credentials('docker_password')
    }

    stages {

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
                DOCKER_USERNAME = credentials('docker_username')
                DOCKER_PASSWORD = credentials('docker_password')
            }

            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }

        stage('Config and deploy') {
            steps {
                sh "scp docker-compose.yaml"
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