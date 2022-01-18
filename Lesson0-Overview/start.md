# Best Practices for Scheduled Jobs

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

<img src="https://dyltqmyl993wv.cloudfront.net/assets/stacks/jenkins/img/jenkins-stack-110x117.png" width="200px">
<img src="https://i.redd.it/tm9debwp5f301.png" width="200px">
<img src="https://thumbs.dreamstime.com/b/computer-servers-24528917.jpg" width="200px">


---vertical---


# The People

<img src="https://legendsrevealed.com/entertainment/wp-content/uploads/2016/10/scottstartrek1-515x386.jpg" width="200px" class="center">

<img src="https://www.esri.com/arcgis-blog/wp-content/uploads/2019/11/Garry_emoji_globe-1-213x200.png" width="200px" class="center">

<img src="https://miro.medium.com/max/1400/1*-Ga24xFA0jHOXvKasE0q2w.png" width="200px" class="center">

* Scott / Harry - needs to keep servers running
* Data Analysts / GIS Analysts / Other - want jobs running on a schedule
* All:
    * Reliability
    * Maintainability
    * Recoverability from Failure

notes: We want to be able to add / remove / replace servers that are
attached to the jenkins service without requiring notification.  When
this happens we want users of scheduled jobs to be unaffected by these
changes.

---vertical---


### How do we get there?

* Define a build step in your deployment
* Install non standard S/W in your build.
* Maintain code in Source Code Repository
* Don't embed secrets in your code
* Log messages to STDOUT
* Use Jenkins Pipeline format vs freestyle projects
*
