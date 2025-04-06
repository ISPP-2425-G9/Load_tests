# Load_tests

This is a project used to make load tests in the backend using Locust.

## Installing local enviroment

You will have to activate a local python enviroment in case that you want to insolate dependencies. You can do this following these steps

### In Linux

``` bin/bash
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

### In Windows

Using command promt

``` bin/bash
python -m venv venv 
.\venv\Scripts\activate
pip install -r requirements.txt
```

Using powershell

``` bin/bash
python -m venv venv 
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```

## How to run tests

In order to run all tests you can run the following command:

``` bin/bash
locust -f locustfile.py
```

If you want to run specific module you can run all modules tests with these commands:

- For running all Admin tests

    ``` bin/bash
    locust -f admin\AdminLoadTests.py
    ```

- For running all Company tests

    ``` bin/bash
    locust -f company\CompanyLoadTests.py
    ```

- For running all Customer Free tests

    ``` bin/bash
    locust -f customer\CustomerFreeLoadTests.py
    ```

- For running all Customer Premium tests

    ``` bin/bash
    locust -f customer/CustomerPremiumLoadTests.py
    ```

- For running both Customer and Customer Premium tests

    ``` bin/bash
    locust -f customer\CustomerFreeAndPremiumTests.py
    ```

## Running just a specific class

If you just want to run one specific class you can do it running only the file or indicating the class

- Selecting the file:

    ``` bin/bash
    locust -f relativeRouteToYourFile
    ```

    Example: locust -f anonymous\status.py

- Selecting the class:

    ``` bin/bash
    locust -f locustfile.py --class nameOfTheClassThatYouWantToRun
    ```

    Example: locust -f locustfile.py --class checkStatus
