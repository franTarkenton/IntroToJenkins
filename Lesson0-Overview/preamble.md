# Best Practices for Scheduled Jobs

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
* Common Interest / what we all want:
    * Reliability
    * Maintainability
    * Recoverability from Failure

note: We want to be able to add / remove / replace servers that are
attached to the jenkins service without requiring notification.  When
this happens we want users of scheduled jobs to be unaffected by these
changes.

---vertical---


## How do we get there?

This training will hopefully be a start!

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

Its a foundation that can be built on.

---vertical---

### Approach

* This course will use python for its demos.
* Concepts covered using python should be transferable to other languages
* Editor of choice for course is vscode
