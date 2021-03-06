# Preamble

<img src="https://lh3.googleusercontent.com/pw/AM-JKLUaMIaTUTjEd5hg1Dw0wkqQzNa2dlqyrk6IK5eamotIne_71Ye13MA-sHVjDlFm6rY7Gt37KN5dEn76xLyVmYvm5877_hZeUffFryClWZUcitH6uBdGiz5FCS37p2oXQh9clQVApD0GBYKHhvwefoZxoQ=w1168-h569-no?authuser=0" width="600px">

---vertical---

## Best Practices for Scheduled Jobs

<img src="https://lh3.googleusercontent.com/pw/AM-JKLWPvuuteO-Y0pii9Ng7Lx-52zuh6rxYeH7BtuZPOBfuehG2bjzYJdCQW0KtFc-MB1D53McaSu18DFHcGLVeWqzCz_6wscihUwj2ixodakRsPGdZOlOfPIeELPYJ9ppd34iDQEOlLy2aFpjBEKaxe1ukVA=w908-h442-no?authuser=0" width="400px">

* Scheduled jobs - recognized as business need
* Been lot of Learning from various past approaches
* Objective: best practices / guidance for scheduled jobs

Note: The need for IIT's clients to be able to schedule jobs has existed for many
years.  Various approaches have been taken over the last decade that attempt to
fill this need.  The most recent iteration has been the creation of the **Jenkins
service for Scheduled jobs.**

Over the past year IIT's has observed some patterns that raise concerns for
our ability to maintain and scale the service.

This course is intended to provide guidance to users of this service around how
scheduled jobs should be created and deployed.

---vertical---

# Implementation

* Jenkins Master node
* Connects to a couple GIS Terminal Server boxes
* Jenkins configuration allows for running jobs with a schedule

<img src="https://dyltqmyl993wv.cloudfront.net/assets/stacks/jenkins/img/jenkins-stack-110x117.png" width="200px">
<img src="https://i.redd.it/tm9debwp5f301.png" width="200px">
<img src="https://thumbs.dreamstime.com/b/computer-servers-24528917.jpg" width="200px">


---vertical---


# The Issue...

*Things will be easier once the machines take over*<!-- .element class="smallersize2left" -->

<img src="https://legendsrevealed.com/entertainment/wp-content/uploads/2016/10/scottstartrek1-515x386.jpg" width="225px" class="center">

<img src="https://miro.medium.com/max/1140/0*gLwoK2E-X1gIgocm" width="300px" class="center">


* Mr. Scott - Lots of servers to manage - no snowflakes
* Data Analysts / GIS Analysts / Other (kirk / spock) - want their code running on a schedule
* Common Interest / what we all want:
    * Reliability
    * Maintainability
    * Scalability
    * Recoverability from Failure

Note: We want to be able to add / remove / replace servers that are
attached to the jenkins service without requiring notification.  When
this happens we want users of scheduled jobs to be unaffected by these
changes.

For the system to work the code needs to be created and deployed in a way
that allows Scott/Harry to:
* add new servers
* swap out servers

With minimum of effort

---vertical---

## How do we get there?

This training will hopefully help get us there!

* Don't embed secrets in your code
* Maintain code in Source Code Repository
* Define a build step in your deployment
* Install non standard S/W in your build.
* Log messages to STDOUT
* Use Jenkins Pipeline format vs freestyle projects

---vertical---

## But we aren't programmers!!??

<img src="https://steenschledermann.files.wordpress.com/2014/05/no-thanks-were-too-busy1.jpg" width="400px">
<br>

* Things are already too complex
* I'm busy, don't have time for this nonsense!
* There has to be an easier way.

Note: If you write code, I consider you a programmer.  We are all at
different levels.  If we approach problems together I believe we can
learn and evolve at much faster rate.

Recognize that we are all overloaded with work and adding a new way of doing
things is a pain and costs time.

Every approach has a trade off!  The ideas / concepts behind this training come
from a long history of experience, where shortcuts have been taken... caused
a lot of pain... and lessons have been learn't.

Ideas are loosly pulled from the 12 factor app: https://12factor.net/

ultimately we have two objectives with this training:
* maintainable service
* Share best practices around how to structure automations

Its a foundation that can be built on.

---vertical---

### Approach

* This course will use python for its demos.
* Concepts covered using python should be transferable to other languages
* Editor of choice for course is vscode
