# Overview

This repository will contain all the lessons / code that
have been used to deliver the Jenkins training to GIS /
Data Analysis staff.

The province of BC has a lot of staff that are familiar
with building ad-hoc scripts that can be run on a
terminal server or desktop computer.  Moving adhoc
scripts to a scheduled service so they can run unattended
based on events, or a time schedule introduces some
of the following issues:

* Service Accounts and associated security issues:
    * script is scheduled it needs to run under a "service account".
    * if script needs to see specific folders the service account needs to be
        configured so it can see those folders.
* Configure servers

Running scripts on a scheduled
