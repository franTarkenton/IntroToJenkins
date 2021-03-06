# Syllabus

<img src="https://lh3.googleusercontent.com/pw/AM-JKLWboMhNfRKNuWp7MY1lQIRrunqa-rpaNnJFqezp0PD-2qKnblIaSWpoy3TGyAf77BRoPhxDMfJqm7TJlSYACChax1bDKGajhER_9AYWNJax-IFRBYtUXNIhn0asAX9fkcQheZQYZn5Xi1_tm7z-d1yAYw=w1168-h569-no?authuser=0" width="600px">

---vertical---

# Pre-requisites

* Some familiarity with python programming language, have used it before
* Have a code base / script that user would like to integrate into Jenkins
* Time / availability to participate fully.

Note: This document describes the concepts that would be included in a proposed
jenkins / cron best practices training course.  The intent of the training is
to take some existing code that users would like to have running in an automated
process, and after the training is complete that code will be polished and
deployed to our Jenkins cron server.

At its core the combined lessons are about how you can share your code, and
define it in such a way that facilitates it being run in a variety of different
places with different input parameters.

Each lesson below will build on the previous lesson, introducing some key
component that will ultimately arrive at a jenkins pipeline script.  Each lesson
will take place over 1/2 a day (roughly 2 - 3.5 hours).  The actual lesson is
expected to take approximately 45 minutes to an hour  to cover.  The remaining
time will be spent applying the concepts covered in the lesson to a code base
that the students will bring to the course.


---vertical---

# Summary of Planned Lessons

* Secrets
* Dependency Management
* Introduction to git / vscode
* Jenkins
* Logging - (Tentative)
* Tools - (Tentative)

---vertical---

### **Lesson 1. Secrets Best Practices**
___

How to keep secrets separate from code, without introducing a lot of overhead
to your code

* Definition of what a secret is
* Using env variables
* Using .env files when doing development
* dotenv python module
* Using secrets with a constants file

---vertical---

### Lesson 2. Dependency Management
___

* Overview of pypi and pip
* how to declare required dependencies
* Case for keeping base install as vanilla as possible
* virtualenv to create an isolated environment
* other approaches pipenv, poetry, conda
* development dependencies vs app / script dependencies

---vertical---

### Lesson 3. Introduction to git / vscode
___

* overview of vscode (kb shortcuts / config / git integration / python )

* What is git vs github
* Cloning a repository
* Remote vs Local repositories
* adding to repository (staging / committing / pushing)
* branches and best practices
* forks


Note: thinking all lessons will cover how to do git operations using vs code gui
as well as with git command line

For branching will discuss best practices using git flow vs github flow.
    * main - always prod ready
    * dev - integration branch
    * feature branches

**Schedule 3 hours for this lesson**

---vertical---

### Lesson 4. Jenkins
___


* overview of jenkins ui
* demo of freestyle project
* introduction to jenkins pipelines
* using pipelines
* Entering secrets into Jenkins Job

Note: Now that we have covered secrets, git, and dependency management
we know enough to take a job and deploy it to jenkins.  This lesson will
focus on the pipeline build, vs freestyle project.

---vertical---

### Lesson 5. Logging (tentative)
___

**Stop using `print` statements**<!-- .element class="smallersize2left" -->

* python logging module overview of components that make it up
* logging config files
* Other ways to configure logging
* playing with log levels

---vertical---

### Lesson 6. tools - Code Linting / Formatting / QA (tentative)
___

* introduction to some commonly used linting tools (flake8, pylint)
* integrate linting with vsCode.
* Code formatting tools (black)
* declaring dev tools used / expected
* Code analysis sonarcloud / radon / xenon
