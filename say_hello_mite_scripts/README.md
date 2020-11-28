# mite scripts for say_hello web app

### Setup
Install [mite](https://github.com/sky-uk/mite).  
Install the scripts module:
```
pip install -e .
```
Update the config file with the host of the package:
 [say_hello_mite_scripts/config/config.py](https://github.com/heliosantos/mite_testing/blob/master/say_hello_mite_scripts/say_hello_mite_scripts/config/config.py)  
```
host  =  'host.docker.internal:5000'
```
Note that the new configuration is not going take effect if the package was not installed in the editable mode.
 
Run scenario1 test
```
mite scenario test say_hello_mite_scripts:scenario1 --config=say_hello_mite_scripts:config
```
