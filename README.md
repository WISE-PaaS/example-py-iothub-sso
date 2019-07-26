# Example-python-Iothub


This is WIES-PaaS iothub example-code include the sso and rabbitmq service。

**https://wise-paas.advantech.com/en-us**

## Quick Start

    git clone this respository
    
    #cf login -skip-ssl-validation -a {api.domain_name}  -u "account" -p "password"
    
    cf login –skip-ssl-validation -a api.wise-paas.io -u xxxxx@advtech.com.tw -p xxxxxx
    
    #check the cf status
    cf target

#### mainfest config
open **`manifest.yml`** and editor the **application name**  to yours，because the appication can't duplicate。
check the service instance name same as WISE-PaaS
![https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/manifest_app_sername.PNG](https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/manifest_app_sername.PNG)
![https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/wise-paas_instance_name.PNG](https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/wise-paas_instance_name.PNG)

open **`templates/index.html`**
    
    #change this **`python-demo-try`** to your **application name**
    var ssoUrl = myUrl.replace('python-demo-try', 'portal-sso');


push application and get environment


    #cf push {application name}
    cf push python-demo-try
    
    #get the application environment
    cf env {application name} > env.json 


    
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

[https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/REAMME.md](https://github.com/WISE-PaaS/example-python-iothub-sso/blob/master/source/REAMME.md)
