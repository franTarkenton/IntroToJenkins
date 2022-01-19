## Lesson 1: Secrets

<img src="https://i5.walmartimages.com/asr/b1d6a172-de39-4cd5-be1f-2614c5d64fdf_1.a6ba6c721e7618a6378fbb547752a5b2.jpeg?odnHeight=450&odnWidth=450&odnBg=ffffff" width="300px">

---vertical---

## Code for this Lesson

<img src="https://lh3.googleusercontent.com/pw/AM-JKLVDxGSgdB8_1dBjYy-DBaBC07wrl0o0WRRjmpfrtzvvkIpVfdROA22rJfteR60g7eEpllD_r839k2fzXW97TcjXflQ5dza6oq4iQjrNX_Z2pxJ0P80lmpAv-Fz5BIHiZVeyZ1JJwP73mGAlIVxsYSGeeQ=w1168-h569-no?authuser=0" width="450px">

* Repository with presentation and code:
https://github.com/franTarkenton/IntroToJenkins

* python code in:
https://github.com/franTarkenton/IntroToJenkins/tree/main/python/Lesson1-Secrets

* or if you have cloned / copied the repo...
`./python/Lesson1-Secrets

---vertical---

<!-- .slide: class="left" element="-->
## Secrets vs Config's

### Secrets:

* password
* api key / token
* *something that gives you access to a system*

### Configurations:

* server names
* file paths
* database instances
* ports
* url's to web services

*For most of this course we are treating them the same way*<!-- .element: class="smallersize1" -->

---vertical---


## Using Environment Variables

<img src="https://lh3.googleusercontent.com/pw/AM-JKLUUWb8HIplUIUo59pXNmv2HzyKeeQPR2SHfbXtESibZ6CCrcRjcQSHiqevzm1l7bc1by7pG5__xJpJO5XVVRVzIpk9EjFPN7pAQK0uSoY3WKB1EeSthmAmnRLC-IW3SHR2hvmZqyLh_A5LCA5WUcMhapA=w1168-h569-no?authuser=0" width="450px">

#### Setting Environment Variables in Windows

```
SET BILLS_PASSWORD=password123!
SET API_KEY=apikey123
```

#### Setting Environment Variables on a Proper OS

```
export BILLS_PASSWORD=password123!
export API_KEY=password123!
```

---vertical---

## Access Environment Variables using Python

```python
import os
password = os.environ['BILLS_PASSWORD']
print(f"Bill's password is {password}")
```
output...
```
Bill's password is password123!
```
example code:<!-- .element: class="smallersize2" -->
  *./python/Lesson1-Secrets/s1_secrets_fromenv.py*

---vertical---


## Using .env Files

* Manually populating environment variables every time you start a new shell can be cumbersome during development
* Using .env files is a common way of storing environment variables during development


**CAUTION** <!-- .element: class="red" -->

* env files contain things you don't want to share
* store them in a separate directory from your code

**OR**

* be **CERTAIN** you have added .env to your .gitignore file

---vertical---

## .env File Format

<img src="https://lh3.googleusercontent.com/pw/AM-JKLWjZCTy5zQEMrCRPEZ24fwubXSZPszve3O8kmv4m4Sn7tQqE24cAdB691EyKsr-1cZTeqb6Ah-wIMqO-oIbDxtx2AdDaJQ9JAOTi2cXnhsieVf90ajOjY0zh5JRM4EIWS_dJfPQsRjuvkG1fvW666yFNQ=w1168-h569-no?authuser=0" width="500px">

Example:
```
BILLS_PASSWORD=password123!
API_KEY=password123!
#COMMENTED_OUT_VARIABLE=lines that start with # are considered commented out
```

---vertical---

## Populate environment variables using .env files

* You can set this up in vscode by using the debugger to run your scripts
https://code.visualstudio.com/docs/python/environments#_environment-variables

* documentation suggests that vscode should be able to load .env files automatically for you.  I've never had any luck with this

* [python-dotenv](https://pypi.org/project/python-dotenv/) makes it really easy to slurp up .env files.

---vertical---

## Installing dotenv on Windows

*We will cover this topic in much more detail in subsequent lessons.  For now just copy and paste if you are wanting to follow along with code* <!-- .element: class="smallersize2left" -->

```
# install virtualenv globally
C:\Python310\python -m pip install virtualenv

# create a virtualenv
C:\Python310\python -m virtualenv venv

# activate the virtualenv
.\venv\scripts\activate.bat

# install python-dotenv into the venv
pip install python-dotenv
```

Note: In windows its common that python has not been added to the PATH environment
variable so you usually need to either add it, or specify the full path to where
the python interpreter can be found.  With windows to activate the virtualenv
there are .bat scripts and if you are a powershell junkie theres a powershell
option as well

---vertical---

## Installing dotenv on a Proper OS

```
# install virtualenv globally
python3 -m pip install virtualenv

# create a virtualenv
python3 -m virtualenv venv

# activate the virtualenv
source ./venv/bin/activate

# install python-dotenv into the venv
pip install python-dotenv
```

Note: pretty much similar to windows only typically on linux the paths
have already been configured so your terminal can find python.  Also to
activate your virtualenv is different.

---vertical---


## Reading .env files with dotenv and python

```python
import dotenv
import os
dotenv.load_dotenv()

password = os.environ['BILLS_PASSWORD']
apiKey = os.environ['API_KEY']
print(f"Bill's password is {password}")
print(f"Bill's api key is {apiKey}")

print("... also don't do this ^^^")
```

*output*:
```
Bill's password is password123!
Bill's api key is 123xyz!
... also don't do this ^^^
```

example code:<!-- .element: class="smallersize2" -->
  *./python/Lesson1-Secrets/s2_secrets_dotenv.py*

Note: there are a lot of different ways you can load .env files into your
terminal / python env.  This is just one of my preferred options.  Other ways
if you are using linux or osx is to define a bash alias that loads any .env
files it finds in the immediate folder.  Google load .env file for more options

---vertical---

# Setting up environment variables as constants.

* adds to what has been demo'd so far
* create a separate constants module where you will retrieve your configs / secrets
* the constants module checks for .env file and loads it if its found
* otherwise it pulls env variables into a constants file

---vertical---

## Constants module for configs / secrets

```python
import os
import dotenv
import sys

# looking for a .env file in the directory that this module is located
envFileName = '.env'
envPath = os.path.join(os.path.dirname(__file__), envFileName)

# if the .env file is found then load it
if os.path.exists(envPath):
    print("loading dot env...")
    dotenv.load_dotenv(envPath)

BILLS_PASSWORD = os.environ['BILLS_PASSWORD']
API_KEY = os.environ['API_KEY']
```

code can be found at: ./python/Lesson1-Secrets/constants.py <!-- .element class="smallersize2left" -->

---vertical---

## Using Constants

<img src="https://lh3.googleusercontent.com/pw/AM-JKLVI_CX_I0jt4faO15qQCQmwNf1uqPAMmCtIgHVkex7Ahp2fMF_ngSh4eqJrJgFUGaJLOROTcYZHUz8XR4SBpkIFsOZtdCzizeGCEvPgMHDPHQaHRYKUyDr7Ze1SUBGGKmh08J60FcOLDuAlpYZc9_JgJg=w1168-h396-no?authuser=0" width="700px">

```python
import constants

# you can now access any of your constants from
# constants module
print(f"bills password is {constants.BILLS_PASSWORD}")
```

note: Advantage to this approach is you could have multiple env files that are
used under different circumstances with a different set of values.  With the
constants method it becomes really easy to swap out which env file you want to
load and the rest of code doesn't have to change.

Again this is just one way that you could accomplish this.  There are other
modules in python that are even more flexible some of those include:
* https://github.com/sloria/environs
* https://github.com/rochacbruno/dynaconf

---vertical---

## Secrets in Jenkins

* All examples so far have demo's how to separate credentials / configs from
  you code in a development scenario
* When ready to run in Jenkins you will define secrets in your jenkins config
* Secrets will then become available to your code at run time through env vars.

---vertical---

## Future Direction for Secrets Management

* [vault](https://www.vaultproject.io/)
* Tons of things you can do with vault.  Relatively new at IIT.
* If interested in playing with this let me know
* longer term is to define how this service can be used.

note: Will try to carve some time away to figure out how vault could be used
to host secrets for GIS scripts.

Great video that provides a great / understandable overview of vault: https://www.youtube.com/watch?v=VYfl-DpZ5wM

