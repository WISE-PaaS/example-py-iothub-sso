# Example-python-Iothub


This is WIES-PaaS iothub example-code include the sso and rabbitmq service。

[cf-introduce](https://advantech.wistia.com/medias/ll0ov3ce9e)

[IotHub](https://advantech.wistia.com/medias/up3q2vxvn3)

[SSO](https://advantech.wistia.com/medias/vay5uug5q6)

## Quick Start


cf-cli

[https://docs.cloudfoundry.org/cf-cli/install-go-cli.html](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html?source=post_page---------------------------)

python3

[https://www.python.org/downloads/](https://www.python.org/downloads/?source=post_page---------------------------)

![](https://cdn-images-1.medium.com/max/2000/1*iJwh3dROjmveF8x1rC6zag.png)


python3 package(those library you can try application in local):

    #mqtt
    pip3 install paho-mqtt
    #python-backend
    pip3 install Flask
    

## Download this file

    git clone this repository

## Login to WISE-PaaS 
    
![Imgur](https://i.imgur.com/JNJmxFy.png)

    #cf login -skip-ssl-validation -a {api.domain_name}  -u "account" -p "password"
    
    cf login –skip-ssl-validation -a api.wise-paas.io -u xxxxx@advtech.com.tw -p xxxxxx
    
    #check the cf status
    cf target

#### mainfest config
open **`manifest.yml`** and editor the **application name**  to yours，because the appication can't duplicate。
check the service instance name same as WISE-PaaS

![Imgur](https://i.imgur.com/4eynKmE.png)

![Imgur](https://i.imgur.com/VVMcYO8.png)

open **`templates/index.html`**
    
    #change this **`python-demo-try`** to your **application name**
    var ssoUrl = myUrl.replace('python-demo-try', 'portal-sso');


push application and get environment


    #cf push {application name}
    cf push python-demo-try
    
    #get the application environment
    cf env python-demo-try > env.json 


    
Edit the **publisher.py** `broker、port、username、password` you can find in env.json

* bokrer:"VCAP_SERVICES => p-rabbitmq => externalHosts"
* port :"VCAP_SERVICES => p-rabbitmq => mqtt => port"
* username :"VCAP_SERVICES => p-rabbitmq => mqtt => username"
* password: "VCAP_SERVICES => p-rabbitmq => mqtt => password"

open two terminal
    
    #cf logs {application name}
    cf logs python-demo-try

.

    python publisher.py

![https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/publish.PNG](https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/publish.PNG)

# Step By Step Tutorial

[https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/README.md](https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/README.md)
