# Overview

<img src="https://lh3.googleusercontent.com/pw/AM-JKLWZtAp61uDthyr0U6pWcSdg9PqfHbERpmuhD2xWOum87AlWEgjauKGxAMbpLTpvb34I_RLxfGEjCO1HPKyHoPXreljlJiYGZZHMlRVhTPgEQoJtrlwQx7nU0R79cxv5E6EhVUJG2QmEluIXUmExYKSNsA=w883-h430-no?authuser=0" width="600px">

Rendered version of this repo is available at:
[https://frantarkenton.github.io/IntroToJenkins/]()

This repository will contain all the lessons / code that
have been used to deliver the Jenkins training to GIS /
Data Analysis staff.

Increasingly staff hired at the Province of BC have some coding
experience running scripts on their laptops.  In some cases staff
want to automate the running of these scripts so they run using a
defined schedule.

Moving an adhoc scripts to a scheduled service can introduce some
of the following issues:

* script is scheduled it needs to run under a "service account". (if script needs access to data / filesystems that needs to be configured)
* if script needs to see specific folders the service account needs
    to be configured so it can see those folders.
* In some cases credentials are embedded in code.
* Logging over time can consume significant space.  Ideally scripts are set up so log levels can be easily adjusted.

# Objective

This course will attempt to share some best practices that will help
staff author their code in ways that make it easy to transition to a
scheduled service.

The best practices defined in this Lesson will also help with writing
code that takes advantage of new and emerging compute platforms like
github actions / serverless computing.

# Running the [Revealjs](https://revealjs.com/) presentation

### Install Node
Install node / npm if not already installed, google *install node npm*
and follow the instructions

### Install Git
Same instructions as ^^^

### Clone this repo
```
git clone https://github.com/franTarkenton/IntroToJenkins
```

### Install dependencies
```
cd IntroToJenkins
npm install
```

### Start the presentation
```
npm start
```





