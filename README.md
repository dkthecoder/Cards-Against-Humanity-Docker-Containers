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

The database for this project currently comprises of a "users" table, a "lists" table and an "items" table. Where one user can have many lists, and one list can have many items. The ERD for this MVP is shown below:  



The goal for future iterations of this project would include additional functionality to mark items as done, archieve lists, share lists amongst other users (almost like a list social network).

Despite the requirments stating the use of a reverse proxy OR a loadbalencer, I personally feel that both could be of benefit (EXPLAIN)!!

## CI Pipeline:  

![JIRA TIMELINE](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/jira%20timeline.png?raw=true)

![JENKINS](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/jenkins%20stage%20view,%20build%20history.png?raw=true)
Due to constraints with storage, the actual total jenkins builds are not shown in the above figure.

Ideally in Jenkins, I would be creating a initial stage of testing application functions first, if passing that, the remaining stages would run. Even better, would be to have Jenkins pull from the dev-feature branch through development, per each commit made, which runs the tests to assess if the build is operable, then creating a branch merge request, which when accepted by the develope, would merge to the "dev/feature" branch to the main, and triggure another pipeline for deployment.


## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. Some of the control measures implemented in the project as a result of the risk assessment are as follows:  

![RA](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/risk%20assessment.png?raw=true)  

The likelihood and impact level (out of 5) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.

## Testing:  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked as intended.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. As mentioned previously, these tests are automated using Jenkins via webhooks. A successful build, in which all tests passed, is shown below:  

![cov](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/coverage.png?raw=true)  
Showing 96% coverage overall. All tests must pass for a build to be successful, a single failed test marks the build overall as failed.


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
