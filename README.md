# Opal Python SDK Script For Removing Empty Permission Sets

## About
This script uses the [Opal Python SDK](https://github.com/opalsecurity/opal-python) to iterate through `AWS_SSO_PERMISSION_SET` type Opal resources and delete any resources that have no associated users. This is a one off script consideration to help with a customer issue.

## How to use

- Make sure you have `python3` version `3.13.7` or above installed
- Clone this repository
- In the terminal, change to the `opal-python-sdk-empty-permission-sets-removal` directory:

Unix Like Systems:
```shell
cd opal-python-sdk-empty-permission-sets-removal
```


Windows:

```shell
dir opal-python-sdk-empty-permission-sets-removal
```
- Make a python virtual environment and activate it:
```shell
python3 -m venv .
source bin/activate
```
- Install dependencies
```shell
python3 -m pip install -r requirements.txt
```
- (OPTIONAL) Replace the host string with your self hosted URL
```python
configuration = opal.Configuration(
    host = "https://api.opal.dev/v1" # Replace with self-hosted domain (e.g. https://opal.example.com/v1)
)
```
- Replace `"ACCESS_TOKEN_HERE"` on line 20 with your access token

```python
configuration = opal.Configuration(
    access_token = "ACCESS_TOKEN_HERE" # Opal Access Token here NOTE: can not be a read-only token
)
```
- Run the script
```shell
python3 opal.py
```