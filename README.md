# EnigmaCMS-Backend

## Server for our Club

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl-125x28.png?v=103)](https://opensource.org/licenses/GPL-3.0/)

## Getting Involved [![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](#)

We encourage you to participate in this open source project. We love Pull Requests, Bug Reports, ideas, (security) code reviews or any other kind of positive contribution. 

Before you attempt to make a contribution please read the [Community Participation Guidelines](https://github.com/partha2000/EnigmaCMS-Backend/blob/main/CONTRIBUTING_guidelines.md).

* [Guide to Contributing code](https://github.com/partha2000/EnigmaCMS-Backend/blob/main/CONTRIBUTING_code.md) (**New contributors read the community guidelines and start here!**)

* [View current Issues](https://google.com)

* [View current Pull Requests](https://google.com)
* or [file a issue](https://google.com)

* Haven't joined our discord server? [join here](https://google.com) to keep up to date.


**Beginners!** - Watch out for [Issues with the "Good First Issue" label](https://github.com/EnigmaVSSUT/EnigmaCMS-Backend/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22). These are easy bugs that have been left for first timers to have a go, get involved and make a positive contribution to the project!

## Languages / Framewoks involved
* __Languages__
  - Python
* __Frameworks__
  - django
  - Graphene
* __Database__
  - MongoDB

## Build Instructions

1. Clone or Download the repository:

  ```bash
  git clone https://github.com/EnigmaVSSUT/EnigmaCMS-Backend
  ```

2. Inside the `Enigma_CMS_backend/project` start the server by entering into the terminal `$ python manage.py runserver`

## Setting up the environment (Linux and MacOS)
_Always make sure you have python 3 and are using virtualenv to install and manage your packages_
__First get into `Enigma_CMS_backend/project` an then follow the steps given below__
1. `pip3 install virtualenv`		-> Install the virtualenv library
2. `virtualenv .venv`			-> Create a virtual environment
3. `source .venv/bin/activate`		-> Get inside the virtual environment
4. `pip install --upgrade pip`		-> get upgraded to pip3
5. `pip install -r requirements.txt`	-> Thereafter install all the packages as per the reqirements.txt


## Setting up the environment (Windows)
_Always make sure you have python 3 and are using virtualenv to install and manage your packages_
__First get into `Enigma_CMS_backend/project` an then follow the steps given below__
1. `py -m pip install --user virtualenv`		-> Install the virtualenv library
2. `py -m venv env`			-> Create a virtual environment
3. `.\env\Scripts\activate`		-> Get inside the virtual environment
4. `pip install --upgrade pip`		-> get upgraded to pip3
5. `pip install -r requirements.txt`	-> Thereafter install all the packages as per the reqirements.txt