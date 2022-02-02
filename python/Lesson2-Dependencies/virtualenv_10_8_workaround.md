# What do I do???

```
H:\>python -m virtualenv venv_test
E:\sw_nt\Python27\ArcGIS10.8\python.exe: No module named virtualenv
```

# Preamble

Ideally you should work with your server admin to get virtualenv
installed as part of the configuration of the server.  Recognizing you
sometimes need to move faster...

Read on!

# Virtualenv not installed Workaround 2 (GTS - 10-8 Desktop)

### Install virtualenv to your profile

```
python -m pip install --user virtualenv
```

This will install to %APPDATA% folder.

# Create and Activate a virtualenv

```
python -m virtualenv <name of virtualenv you want to create>
./<name of virtualenv you want to create>/Scripts/activate
```


# Virtualenv not installed Workaround 2 (GTS - 10-8 Desktop)

* If you want more flexibility this option allows you to install the virtualenv or any module wherever you want.

In code below we will install python to directory called **virtualenv27**

To start open cmd

open cmd
```
<driveletter>:
cd <location to install>

mkdir virtualenv27
python -m pip install -t ".\virtualenv27" virtualenv
SET PYTHONPATH=%cd%\virtualenv27;%PYTHONPATH%
python -m virtualenv venv
.\venv\Scripts\activate
```

# Install virtualenv to your virtualenv

Finally, if you wanted to have your own virtualenv that also
has the module virtualenv installed in it, the following shows you
how:

start with a new cmd window:
```
<driveletter>:
cd <location to install>

.\venv\Scripts\activate
pip install virtualenv
```




Now you can use this as your starting virtualenv.

```
import archook
archook.get_arcpy()



