# Steps to setup in Local
+ Clone using git clone git@bitbucket.org:tribes-ai/transform-load-data-python-3.git
+ Install the [virtualenv](https://pypi.org/project/virtualenv/)
+ Create a virtual environment using the command : virtualenv <name-of-environment> --python=python3
+ Activate the virtual environment using the followiing command :

**In Windows**

source <name-of-env>/Scripts/activate.bat

**In Linux**

source <name-of-env>/bin/activate
+ Install requirements by using the command pip3 install -r requirements.txt
+ Set environment variable GOOGLE_APPLICATION_CREDENTIALS to the location of service account key.
+ Run main.py
