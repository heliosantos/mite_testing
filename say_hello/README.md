# say_hello

A web application which says hello to visitors.

### Installation

Install the application (tested on python 3.7)
```
pip install -e .
```

Set an environment variable to tell flask the application name:

on Linux
```
export FLASK_ENV=say_hello
```

on Windows
```
set FLASK_APP=say_hello
```

Run the application on the default host/port (http://localhost:5000). 
```
flask run
```
To change the host and/or port pass the following arguments to flask `--host=[host]` `--port[port]`
