# Cards Against Humanity, Docker Containers:
Cards Against Humanity (abbreviated as CAH) is a fun, creative commons-licensed card game in which players complete "fill-in-the-blank" statements yusing words or phrases rich are typically, offensive, risqué or politically incorrect. I aim to take this fun and enriching cardgame and convert it into a python based web-app which deploys as 4 distinct microservices across containerised mediums.

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
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. 


## App Design:  
To conform with the project requirments, the application needed to have four distinct services. These services operate together as microservices which interact with each other using GET/POST requests/responces. The services used are:
* service1frontend: operational end shown to the user.
* service2blackcards: 
* service3whitecards:
* service4magicmaker:

This structure is represented below:  
![MICROSERVICE FRAMEWORK](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/CAH%20framework.png?raw=true)  

## Deployment Design:
To demonstrate CRUD, I have chosen to build a list-making application, which allows users to:
* CREATE an account, lists and items within a list
* READ account details, lists and items of that list which belong to the user
* UPDATE a users account details, a list with items
* DELETE users account, lists and items within a list

The database for this project currently comprises of a "users" table, a "lists" table and an "items" table. Where one user can have many lists, and one list can have many items. The ERD for this MVP is shown below:  

![CONTAINER DEPLOYMENT](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/CAH%20cluster%20deploy%20diagram.png?raw=true)

The goal for future iterations of this project would include additional functionality to mark items as done, archieve lists, share lists amongst other users (almost like a list social network).


## CI Pipeline:  
![KANBAN BACKLOG]()

![KANBAN TIMELINE]()

![JENKINS]()
Due to constraints with storage, the actual total jenkins builds are not shown in the above figure.

Ideally in Jenkins, I would be creating a initial stage of testing application functions first, if passing that, the remaining stages would  run. Even better, would be to have Jenkins pull from the dev-feature branch through development, per each commit made, which runs the tests to assess if the build is operable, then creating a branch merge request, which when accepted by the develope, would merge to the "dev/feature" branch to the main, and triggure another pipeline for deployment.


## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. Some of the control measures implemented in the project as a result of the risk assessment are as follows:  

![RA](https://github.com/dkthecoder/Cards-Against-Humanity-Docker-Containers/blob/main/figures/risk%20assessment.png?raw=true)  

The likelihood and impact level (out of 5) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.

## Testing:  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked as intended.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. As mentioned previously, these tests are automated using Jenkins via webhooks. A successful build, in which all tests passed, is shown below:  

![build]()  
The coverage reports, showing what percentage of statements were included in the tests, were output as html files, which were archived post-build. The coverage report for the above build was:  

![cov]()  
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

## Future Work:
* Custom error pages.
* Design for mobile display (for mobile web-app deployment).
* User accounts to retain custom cards.
* Modals for confirmation prompts.
