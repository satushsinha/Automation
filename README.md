# Steps to setup in Local
+ Clone using ```git clone git@bitbucket.org:tribes-ai/transform-load-data-python-3.git```
+ Install the [virtualenv](https://pypi.org/project/virtualenv/)
+ Create a virtual environment using the command : ```virtualenv <name-of-environment> --python=python3```
+ Activate the virtual environment using the followiing command : ```source <name-of-env>/bin/activate```
+ Install requirements by using the command pip3 install -r requirements.txt
+ Authenticate the Google Cloud API, For details refer this [Google Cloud Authnentication](https://cloud.google.com/docs/authentication/getting-started)
+ Set up the Cloud proxy to connect to cloud SQL, For setup instructions refer this [Cloud Proxy Setup](https://cloud.google.com/sql/docs/mysql/quickstart-proxy-test)
+ You may require some cloud SQl details, You can see SQL instances [here](https://console.cloud.google.com/sql/instances?authuser=5&project=tribes-ai-development)
+ Set up the required [enviroment variables](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.)
+ Run main.py
