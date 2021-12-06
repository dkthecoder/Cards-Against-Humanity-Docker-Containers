# Cards Against Humanity, Docker Containers:
Cards Against Humanity (abbreviated as CAH) is a fun, creative commons-licensed card game in which players complete "fill-in-the-blank" statements using words or phrases rich are typically, offensive, risqué, or politically incorrect. I aim to take this fun and enriching card game and convert it into a python-based web-app which deploys as 4 distinct microservices across containerised mediums.

This repository is also part of the deliverables for the QA devops project 2 and thus, will aim to split the application across 4, deployable "Docker" containers from a script.

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [Deployment Design](#Deployment-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [App Screenshots](#App-Screenshots)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to develop an application which is split over 4 distinct microservices and can be deployed in a containerised manner across virtual machine clusters on any given cloud platform. Ideally, this deployment should be automated and through a pipeline. Notable tools include Docker Compose/Swarm, Jenkins and ansible.CRUD (create, read, update and delete) functionality was not required but was highlighted as a feature that would yield brownie points. These services operate together as microservices which interact with each other using GET/POST requests/responces. 

## App Design:  
The structure is represented below:  
![MICROSERVICE FRAMEWORK](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/CAH%20framework.png?raw=true)  

The services used are:
* service1frontend: Displying the web-app, handling user inputs and display of information.
* service2blackcards: Loads black card deck, handles CRUD actions.
* service3whitecards: Loads White card deck, handles CRUD actions.
* service4magicmaker: Takes input to generate random numbers.

As documented in the diagram, I have placed nginx as part of the deployment, a fifth microservice is placed prior to the frontend. This is a docker container running nginx as a reverse proxy can hide the topology and characteristics of your back-end servers by removing the need for direct internet access to them. This allows a single, externally reachable endpoint, protecting the microservices from being snooped or exploited.

## Deployment Design:
The deployment is represented below:  
![CONTAINER DEPLOYMENT](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/CAH%20cluster%20deploy%20diagram.png?raw=true)

Given the requirements of the project, GitHub would be the intermediary between my local machine and the Jenkins VM which would pull from GitHub and construct the docker containers and deploy the containers to the docker swarm manager. Ansible would then configure the machines as and when needed as a new build was requested.

As illustrated, there are three docker swarm VM's. One manager and two other workers, though, a second worker is optional. each worker (including the manager) would contain duplicates of the microservices for redundancy, ensuring high availability. within each worker, the containers of each microservices communicate within their own local network, which would be accessed via the reverse proxy (as established earlier). when accessed by users, they are not specifically coerced to use a worker or manager hosted services but would connect to whichever is available.

Despite the requirements stating the use of a reverse proxy OR a load balancer, I personally feel that both could be of benefit, not only having the added layer of security from the reverse proxy, but the means to balance the distribution of users across swarms rather than allowing this to randomly occur by itself.

## CI Pipeline:  
For managing the projects development, I had chosen to use Jira for mapping out the required tasks to be completed, and to organise each task into sprints over a given time horizon. Below is a screen capture of how the sprints looked over a timeline, showing the overall, estimated completion of tasks and their respective sprints.

![JIRA TIMELINE](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/jira%20timeline.png?raw=true)

In order to meet the requirments of the project, Jenkings was utilised to operate a Continuous Development/Continuous Deployment pipeline. Orchestrating the git repo pull, construction of docker containers and orchestration of the docker swarm manager/worker on their respective VMs. Below is a screen capture of the Jenkins build timeline through project development, as well as the associated pipeline:

![JENKINS](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/jenkins%20stage%20view,%20build%20history.png?raw=true)

Due to constraints with storage, the actual total jenkins builds are not shown in the above figure but are greater than the current number suggests. To save on storage, most older builds were deleted.

Ideally in Jenkins, prior to building the docker containers, I would have an initial testing stage in order to assure the functionality of the app worked. Only if passing that, the remaining stages would run. Even better, I'd have created a separate repository branch just for Jenkins to pull from when a commit was made and run specific tests to assert functionality. If the tests would pass, a branch-merge request to a dev or main branch. Which when accepted, would trigger another pipeline for deployment.

## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. Some of the control measures implemented in the project as a result of the risk assessment are as follows:  

![RA](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/risk%20assessment.png?raw=true)  

The likelihood and impact level (out of 5) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.

## Testing:  
Testing the app was an essential part of the development process. However, I had only chosen to pursue one type of testing: Unit tests. This type of testing tests the functional elements of the each microservice through inputting information and assessing its output over predetermined results, to determine if the function does what it intends to do. Below is the coverage report for each microservice:

![cov](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/coverage.png?raw=true) 

The average coverage is sub-par and is mainly affected for the lack of testing implemented. Mainly, I missed out "mocking" the connection to test the function with. Resulting in disappointing coverage and a low-test result. Further to this, I had decided to perform tests outside of the pipeline, which is not ideal and should really be part of the deployment pipeline to catch bugs.

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. As mentioned previously, these tests are automated using Jenkins via webhooks. A successful build, in which all tests passed, is shown below:  

## App Screenshots:  
Below are screenshots of the app functioning:

![CAH INDEX RULES LETSPLAY](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/screenshots/CAH%20index%20rules%20lets%20play.png?raw=true)  
![CAH BLACK WHITE CARDS](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/screenshots/CAH%20black%20white%20cards.png?raw=true)  

## Known Issues:
* No HTTPS, can be enabled given a domain for Certbot and Nginx.
* Issues with storing DateTime into database causes an error. This issue occurs randomly.
* Delete functionality is faulty.
* When creating desacription for new list, using grammer may cause SQL errors.
* Secrets are passed through "sh" using Groovy String interpolation which is insecure.
* Depsite successful pipeline deployment, service4magicmaker seems to fail to start within the docker swarm.

## Future Work:
* Custom error pages.
* Design for mobile display (for mobile web-app deployment).
* User accounts to retain custom cards.
* Modals for confirmation prompts.
* Implement a load balancer.
