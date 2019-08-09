
<p align="center">BackTest</p>
<p align="center">Open source backtesting tool.</p>

# Table of Content
+ [Getting Started](#getting_started)
+ [Built With](#built_with)
+ [File Structure](#file_structure)
+ [Authors](#authors)


## Getting Started<a name="getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Ensure that python 3.6 or higher and pip are already installed on the system<br>
Further instruction for installing the above can be found at [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)<br>

### Installing

A step by step series of examples that tell you how to get a development env running

Cloning the repo
```
$ git clone <repo link>
```
Installing the dependencies
```
$ cd BackTest
$ sudo apt-get install python3-pip
$ pip install -r requirements.txt
```
If you want to use additional charting patterns(DOJI,MARUBOZU,etc) or indicators from the TA-Lib library, install the ta-lib python wrapper
```
pip install ta-lib
```
Note: This requires the underlying TA-Lib library to already be installed in your device. See [TA-Lib](https://mrjbq7.github.io/ta-lib/install.html) for further instructions.
Running the server
```
$ gunicorn --workers (2*<number of cores>+1) --bind 0.0.0.0:5000 wsgi:app
```
The application will now be running on https://<your_IP_Address>:5000/

## Built With<a name="built_with"></a>
+ [Python](https://www.python.org/) - Language
+ [Flask](https://palletsprojects.com/p/flask/) - Server Framework
+ [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server for UNIX
+ [Backtrader](https://www.backtrader.com/) - Backtesting module
+ [TA-Lib](http://ta-lib.org/) - Technical Analysis Library

## File Structure <a name="file_structure"></a>
/BackTest.py  : Main server code <br>
/templates/  : Website code <br>
/FetchData.py     : Backtesting Script <br>

## Authors<a name="authors"></a>
+ [Roshan James](https://github.com/sephiroth7712) <br>
+ Suraj <br>
+ [Mayur Kadam](https://github.com/mayurkadampro) <br>
+ Rajendra Vinod Patil<br>
