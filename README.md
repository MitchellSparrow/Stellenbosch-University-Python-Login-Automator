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

### 1.) learn 
To launch Sunlearn in a new tab in chrome

### 2.) ilearn      
To launch Inetkey and Sunlearn in seporate tabs in chrome

### 3.) i           
To launch AND sign into Inetkey using the "Chrome Driver", then MINIMIZE this window

### 4.) l           
To launch AND sign into Sunlearn using the "Chrome Driver", then MAXIMIZE this window

### 5.) il          
To launch AND sign into Inetkey AND Sunlearn using the "Chrome Driver", then MAXIMIZE this window

The following is an example of how to run this python file:

```bash
python myinternet.py learn
```

### When using the chromedriver commands such as "i" or "il":

Replace the following lines below with your username and password. It is however recommended that you rather create and utilize a private, secure file where this sensitive information is stored and then import these values from that file. 

```python
username = "username"  # Enter your username here
password = "password"  # Enter your password here
```

## Further Automation

To make this process even simpler, you can create a BASH file and add this file to your path. This means that you can run this file from anywhere in the command prompt.

### For example:

I created a "internet.bat" file and added the location of this file to my path.

The contents of this file were as follows:

```bash
@echo OFF

cd C:\Path\To\Your\Python\File
myinternet.py %1 %2 %3 %4
cd C:\Users\"Your User Name"
```

This meant that I could run the following commands from anywhere in the command prompt which made the process quicker:

```bash
internet learn
internet ilearn
internet i
internet l
internet il
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)