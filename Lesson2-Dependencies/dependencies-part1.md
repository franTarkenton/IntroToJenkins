
## Lesson 2

### Handling Dependencies with Python

<img src="https://lh3.googleusercontent.com/pw/AM-JKLUse9RcKF_KgC1iNKiN0_1r5em9ro0eqlVu5K-cw83_IElFjwTf24aiMRjGsqWxgCyG9x7cuT1XcBEsxHuf8_f1Tz8jsBOx4lC0EriEHwMiAbStwDQxJZuKhO3PZaqfP937sZCY5Pfv1CsiA37OeNbH-g=w957-h718-no?authuser=0"
width="500px">

---vertical---


## Code for this Lesson

<img src="https://lh3.googleusercontent.com/pw/AM-JKLVpjK4tF7Bil7hcTBPnIsae5SKsWtDjFFNHzcpG8ACz0CLMjpvXIazaj2cOY6VgvnRUAmkd0WI8qo3DavzUWTYg_2B4Bdp5c8bhwKoqeVZ7k_JmkMNfQAyF_5286MZqjKslOBDTtPhEQbCMsr8alp3Ttw=w862-h420-no?authuser=0" width="400px">

<!-- .element: class="smallersize2" -->
* Repository with presentation and code:<!-- .element: class="smallersize1" -->
https://github.com/franTarkenton/IntroToJenkins<!-- .element: class="smallersize1" -->

* python code for this lesson:<!-- .element: class="smallersize1" -->
https://github.com/franTarkenton/IntroToJenkins/tree/main/python/Lesson2-Dependencies<!-- .element: class="smallersize1" -->

* or if you have cloned / copied the repo...<!-- .element: class="smallersize1" -->
`./python/Lesson2-Dependencies<!-- .element: class="smallersize1" -->

---vertical---

### Dependencies: how they related to Scheduled Jobs

#### Objective: Best Practices for Jenkins / Scheduled Jobs

  * ~~Separation of secrets~~ - **Done**
  * Separation of dependencies - **Today**
  * Code in source code repository - **Upcomming**
  * Putting it together with Jenkins - **Upcomming**

*Ultimately scheduled jobs run in disposable environments, with clearly defined build steps*

---vertical---

## High level flow of Jenkins job trigger

<img src="https://lh3.googleusercontent.com/pw/AM-JKLU0jxQH6bpHnwIhztUY6g07R0DyUEN-m2jTWGxXJXczz4Ks7N8jPaGHh1_z_SGCDvMVV0Jv2oCNDrFxYplVI8nqg8j6-1hhVq5uVvsuz3IwZOLHtxGvI9hOQhUzUAM-13xT0JFxj23PU-BO5ykkTDR9SQ=w261-h175-no?authuser=0" width="500px">

note:

Jenkins master - coordinates the running of jobs, detects that its time to run a job and then sends a bundle of information about a job over to a jenkins agent.

---vertical---

### Hieroglyph of Desired Jenkins Job Execution

<img src="https://lh3.googleusercontent.com/pw/AM-JKLUWWQ9Sq7GkDSdDalIyoC61saIXn9EXDgk0v-PDioeF9qZIxGyG7d2e3Dp2VHo7smX3jLg_fFmNrblflWVLAcEcLF0G3mwjqQJEzq2Slo-rPVEI7Iu-crlZ-tooUNVfdIUHvUS5k5v5pmoNG6PFxpXuzA=w414-h401-no?authuser=0" width="500px">

note:

Shows what happens on the agent.  The rectangle represents the actual jenkins job, and the ideal flow of what components should be defined for the job.

Recognize that object storage flow is not something that is currently in practice.  The advantage of using object storage for persisted data over
file systems is its much easier to manage access with api keys to object
storage vs cumulatively adding permissions to the service account that the
agent runs under


---vertical---

<!-- .element: class="smallersize1" -->

### Lesson Overview

<img src="https://lh3.googleusercontent.com/pw/AM-JKLUd-ZWzGR7-eKQhhUaoX04l-bAkYB0ySQPAZNS6a6CLBkq4_6EoXe8NH-cyVZMdNpFpEcvAK9hf8-4lTPGReT350taF192KADqHXYXaUoie1iVRqQQ69W3WIrjfI-pYUehH0TQIvY3m6JB8yySH-fJDtQ=w957-h275-no?authuser=0"
width="500px">

* Dependencies - Definition
* Environment isolation
* Tooling / Technical - How to
* Hacking ESRI's conda install
* Putting it together with a demo

note:
* gonna start with high level concepts
* Gradually work from concept to code
* Initially will show code in slides
* Finish up with a start to finish problem

---vertical---

## Dependencies

#### What is a dependency:

* Code that your application uses that isn't in your code repository.
* Usually installed through some kind of package manager.
* Dependencies can also be less formal, pulling in code from another project
* Dependency could also be an entire software package

Note:
ideally we are trying to achieve the relational database dream with code.
in that code is managed in only one location.  Ideally a github repo.

The ultimate solution is:

* a github repo with your code dependencies
* a github action configured for merge to master/main that builds and publishes a pypi package
* The dependency is installed through pip.

---vertical---

 <!-- .element: class="smallersize1" -->

## Python Dependencies

<img src="https://lh3.googleusercontent.com/pw/AM-JKLW_UGuDapR74m41bOYfjg1G4SQ6BFAyF1tw_ZWryinV60I_KMBKzrUonrI1Yo8yWR38YjY3cdSYtDfGGu6-22To3fJsmzIhzPX9BxwlWtNmcoCM_9EvmnmjVXnPnbwNMfN6WOIvPHPB1R8SQVDsYox0Sg=w957-h718-no?authuser=0"
width="400px">

* Most common location of dependencies is [PYPI](https://pypi.org/)  <!-- .element: class="bulletsindent" -->
* By default `pip` installs from pypi
* Can also have a self hosted pypi or use something like artifactory
* Put code that is being re-used into pypi!

*Can't think of many good reasons to deviate from using pypi*

---vertical---

### Software Dependencies

*Your Script needs some software package*

* Ideally figure out how to do a non admin headless install
    * use curl to pull package down
    * cmd or powershell to install in a headless unattended way.
* other option is work with Scott / Harry about whether software is a candidate to be added to a GTS pool

Note:
an example of a software package could be a simple binary dependency like
wgrib2 - https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/

Figuring this out is something you will need to work out on your own.  Usually
a google search for "<software name> headless install" will yield some ideas.

---vertical---


### Why should I care about Dependencies

* Days of relying on someone else to install / manage dependencies on a server are over.
* Self installation into global config on a server creates a mess
    * Each server eventually has its own config.
* increased complexity as scripts need to consider whether dependencies exist or not

note:
Having a clearly defined build process that gathers all the requirements for you
script and installs them, makes your script highly portable.  Transitioning out
of jenkins should be easy.

---vertical---

### Handling Dependencies in Jenkins

<img src="https://lh3.googleusercontent.com/pw/AM-JKLU6z7zTZ9gqP_WTScdoOWWLfhOGNW6NupSd1jvIcbpLvwKlBeyuEkTiWEe9Jg9bUShZU5m-FGXpTeIMC4ufiObNHOQesCQyhPxBMZCanGlGNv6JCD0WXDRz4msKRYPd0R1s8Shj-b0K4IksJ-C0rGAlEg=w957-h713-no?authuser=0"
width="300px">

* Doesn't assume custom software to exist on server
* Include logic to install all dependencies
* Is specific about versions of dependencies
* assume disposable environment - build - run - delete


note:
defining a clear build process that gathers all your dependencies and organizes
them so that they are their for your script ensures your script will run
regardless of what server it gets load balanced to.

---vertical---

### Python specific Tooling

* Python has a number of different tools / options for creating isolated environments
  * virtualenv(python27) / venv(python3)
  * conda / anaconda
  * pipenv
  * poetry
  * pyenv
  * etc...

This lesson will use virtualenv / venv.  Concepts approaches are similar with other tools.

note:
isolated environment = A way of installing python based dependencies without
impacting the global environment.

---vertical---

# Technical Overview

#### Whats comming up next

<img src="https://lh3.googleusercontent.com/pw/AM-JKLWDEFSB_zwS5DJSVMu6giEVNCE6XiAX9bhb5x0c6E92fxFm5wThEdCStlo-OLKWdur5y6dy2wg70AwX43cFII5at4roQdM-0ZFaHXu6XxRqp9m-u2xIGOHN8Ql2BSYfv9IY19h6i3r1K7vtRq-ba5i9Pg=w957-h718-no?authuser=0"
width="300px">
<br>

<!-- .element: class="smallersize1" -->

* create a virtualenv
* install dependencies into the virtualenv
* declare / define dependencies and versions of dependencies

---vertical---

<!-- .element: class="smallersize1left" -->
### Creating a virtualenv:

#### Using python 27:

`python -m virtualenv myvirtenv`

#### Using python 3:

`python -m venv myvirtenv`

If you are getting this error:   `No module named virtualenv`
Install into your user profile:

`pip install --user virtualenv`


note:

Don't make a habit of installing modules into your user profile
Ideally this should be the only exception to that rule.

Notes on other approaches that can be taken to installing virtualenv exist
in the document in the python folder: Lesson2-Dependencies/virtualenv_10_8_workaround.md

---vertical---

<!-- .element: class="smallersize1left" -->

### Activate a Virtualenv

#### Windows:

`.\myvirtenv\Scripts\activate`

#### Proper OS (linux, unix, osx)
`source ./myvirtenv/bin/activate`

#### Windows / Linux prompts with activated virtualenvs

`(venv_win) W:\srm\vic\imb\Workarea\ssharp\venv>`<!-- .element: class="smallersize2left" -->

`(venv_lin) ssharp@NCC-1701:~/proj/jenkinsTraining_newrepo$`<!-- .element: class="smallersize2left" -->


---vertical---

<!-- .element: class="smallersize1" -->

### Virtualenv - Installing Dependencies


<img src="https://lh3.googleusercontent.com/pw/AM-JKLUOfesQwzmfLgGsyv0jS6R4w4bP_zOIv1g-5kRx1AMIMFOGZFbkedv8SV4HwaAeDGuBbv1HEWRBoMC8fhiNXuQ9yV86y4l952CDfzZHMxKE9lZukjNpKOiALjPJl3qVR1228LVeg_DrjJAwrQHzP0qoVg=w957-h425-no?authuser=0"
width="450px">

* first make sure you have activated your virtualenv
* install your dependency using pip

`pip install <dependency name>`

specifically installing `python-dotenv`

`pip install python-dotenv`

note:
you can also uninstall modules from a virtualenv
`pip uninstall <modulename>`

---vertical---

### Declaring your dependencies

* python uses a `requirements.txt` file to declare the dependencies required by your script
* Be specific about versions
* example of a requirements.txt file

```
requests==2.27.1
python-dotenv==0.19.2
archook-dbc==202202.1.2045
xlrd3==1.1.0
minio==7.1.2
```

note:
* the name 'requirements.txt' for the file is by convension.  You can call it
  anything you want

---vertical---

<!-- .element: class="smallersize1" -->

### Development Dependencies vs Script Dependencies

* **Development dependencies**: tools that support development
* Not required for the script/app. to run
* instead they are helpful while building your code.
<br><br>

#### Examples of Dev dependencies
* Linters (pylint, flake8, mypy, prospector, etc)
* Formatters (autopep8, black, yapf)
* Code analysis tools (sonarqube, radon/xenon, mccabe)

*all above are installed also using pip*

---vertical---


### Declaring Development Dependencies

* create a separate file for development dependencies: requirements-dev.txt

Example of a requirements-dev.txt file:

```
flake8==4.0.1
black==22.1.0
radon==5.1.0
```


---vertical---


<!-- .element: class="smallersize1left" -->

### Installing dependencies from a requirements file

* again.. make sure your virtualenv is activated

`pip install -r <path to requirements file>`

usually looks like:

`pip install -r requirements.txt`

---vertical---

### Using Virtualenv on GTS ArcGIS Geospatial - Overview

* ESRI / ArcAmateur uses conda.
* Conda great for packaging up binary dependencies.
* Conda is VERY heavyweight - envs are big and slow to create / load
* Lightweight env's like Virtualenv allow you install just whats required for a specific task
* Combining conda envs and virtualenv is hacky, but it can be done

---vertical---

### Using Virtualenv on GTS ArcGIS Desktop - technical

##### setup
```
python -m venv venv_arcpro
.\venv_arcpro\Scripts\activate
pip install archook_dbc==202202.1.2045
```

#### code
``` python
import archook
archook.get_arcpy(pro=True)
import arcpy
```

note:
If you have no dependency requirements then don't bother with the above.  This
is only if you want to use arcpro with other python dependencies without having
to create another massive conda environment just to do that.

This approach will currently generate a bunch of warning text that can safely
be ignored so long as the code continues to run.  The python detects that
its running from a conda env and lets you know that it hasn't been activated.

That's ok, because we are using a virtualenv that relates to the conda env.  The
module archook is essentially doing the same thing that conda does when it
is activated.

---vertical---


# Using Virtualenv on GTS ArcAmateur - DEMO

Summary of what we are going to do:
* clone the github repo with this presentation
* create a virtualenv
* install dependencies defined in a requirements.txt file
* populate the secrets required to run
* run the process

---vertical---

### Other Advanced Topics

* pip does not address version incompatibility
* example:
   * my-magic-mod version 2.3.42 is installed
   * requirements.txt asks for 2.4.2

pip will see that the dependency my-magic-mod has been met, but doesn't look
at the versions.

* [pipconflictchecker](https://github.com/ambitioninc/pip-conflict-checker) - Great tool that will tell you if you have version conflicts
* [pipdeptree](https://github.com/naiquevin/pipdeptree) - reports on dependency conflicts
* [pipcompile](https://github.com/jazzband/pip-tools/) - prevents conflicts from arising

Note:
for jenkins / automated scripts its unlikely you will run into these issues, but
its good to know that there is tooling to help, if it should happen.

---vertical---

# Related tools / topics worth digging into

* [pipenv](https://pipenv.pypa.io/en/latest/) - combines functionality of pip / virtualenv into a single tool.
  * similar to npm, generates dependency list as they are added
  * creates a Pipfile and Pipfile.lock

* [poetry](https://python-poetry.org/) - similar to pipenv

* Start thinking about packaging your code for inclusion in pypi
* Use github actions to do this automatically for you.

---vertical---

# Useful links:

* [Great tutorial on various dependency / environment tools](https://docs.python-guide.org/dev/virtualenvs/)
* [The full details on version conflicts in python](https://medium.com/knerd/the-nine-circles-of-python-dependency-hell-481d53e3e025)

---vertical---

# Questions?
