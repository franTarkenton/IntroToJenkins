## Secrets

<img src="https://i5.walmartimages.com/asr/b1d6a172-de39-4cd5-be1f-2614c5d64fdf_1.a6ba6c721e7618a6378fbb547752a5b2.jpeg?odnHeight=450&odnWidth=450&odnBg=ffffff" width="300px">

---vertical---


<!-- .slide: class="left" element="-->
## Secrets vs Config's

### Secrets:

* password
* api key / token

### Configurations:

* server names
* file paths
* database instances
* ports
* url's to web services

*For most of this course we are treating them the same way*<!-- .element: class="smallersize1" -->

---vertical---


### Using Environment Variables

#### Setting Environment Variables in Windows

```
SET BILLS_PASSWORD=password123!
SET API_KEY=apikey123
```

#### Setting Environment Variables Proper OS's

```
export BILLS_PASSWORD=password123!
export API_KEY=password123!
```

---vertical---

### Access Environment Variables using Python

```python
import os
password = os.environ['BILLS_PASSWORD']
print(f"Bill's password is {password}")
```
output...
```
Bill's password is password123!
```

---vertical---


### Using .env Files

* Manually populating environment variables every time you start a new shell can be cumbersome during development
* Using .env files is a common way of storing environment variables during development

** Caution **
* env files contain things you don't want to share
* store them in a separate directory from your code
* **OR**
* be **CERTAIN** you have added .env to your .gitignore file





