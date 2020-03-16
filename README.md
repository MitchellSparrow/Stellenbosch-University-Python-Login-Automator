# Stellenbosch University Python Login Automator

The following python file uses Python and Selenium to automate launching and signing into either Inetkey, SUNLearn or both of these. 

## Installation

### Step 1:

Install the latest version of [python 3](https://www.python.org/downloads/) and make sure to add it to your [windows path](https://geek-university.com/python/add-python-to-the-windows-path/)

### Step 2:

In order to use this python script you will need to install the Selenium library using the following command in the command prompt:

```bash
pip install selenium
```

### Step 3:

Download the [chromedriver](http://chromedriver.chromium.org/), unzip the folder and move the .exe file to a folder such as C:\Windows so that it can be accessed in any folder in which you are in


## Usage

The following file takes arguments as an input, this means that when you run the file you will need to provide one of the following commands:

learn       - to launch Sunlearn in a new tab in chrome

ilearn      - to launch Inetkey and Sunlearn in seporate tabs in chrome

i           - to launch AND sign into Inetkey using the "Chrome Driver", then MINIMIZE this window

l           - to launch AND sign into Sunlearn using the "Chrome Driver", then MAXIMIZE this window

il          - to launch AND sign into Inetkey AND Sunlearn using the "Chrome Driver", then MAXIMIZE this window


```bash
python myinternet.py 
```

Replace the following lines with your username and password. It is recommended that you rather create and utilize a private, secure file where this sensitive information is stored and then import these values from that file. 

```python
username = "username"  # Enter your username here
password = "password"  # Enter your password here
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)