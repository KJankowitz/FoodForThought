# Food For Thought Django Project
*A django website that captures recipies in a blog format and has a polling feature to vote on recipies.*

## Table of Contents
1. Introduction
1. Installation
1. Usage
1. Credits and Highlights

## Introduction
This project gathers recipies in the format of a blog with database elements. For user interaction, there is also a polling 
function to vote on recipies. Authorisation practices are followed, and users need to be registered and logged in to vote on the polling app.
This project uses Django with sqlite for database handling and Bootstrap for styling and is packaged in a Docker container. 

## Installation

* Steps
  * Clone this repository: git clone https://github.com/kjankowitz/FoodForThought.git
  * Navigate to the project directory: cd FoodForThought
  * To run **locally** :
    * Create a virtual environment: python -m venv venv
    * Activate the virtual environment:
    * On Windows: venv\Scripts\activate
    * On macOS/Linux: source venv/bin/activate
    * Install project dependencies: pip install -r requirements.txt
    * Run database migrations: python manage.py migrate
    * Start the development server: python manage.py runserver
  * To run in the **Docker container**
    * docker build -t kardo10/food-for-thought .
    * docker run -p 8000:8000 kardo10/food-for-thought

  * Create your own Django Secret Key (if necessary) by using the following python code:
    `from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())`


## Usage
This can be used to collect recipies and gather data on which ones are the most popular.
![First Page](/First_page.png)
![Second Page](/page2.png)
![Third Page](/page3.png)
![Fourth Page](/page4.png)



## Credits and Highlights
Django Documentation: The official Django documentation was incredibly helpful during development 🚀
HyperionDev Bootcamp: The documentation and guidance from this bootcamp was extremely useful 🔥
