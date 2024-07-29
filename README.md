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
This project uses Django with sqlite for database handling and Bootstrap for styling. 

## Installation
* Prerequisites
  Before you begin, ensure you have the following installed:

  * Python 3.x
  * Django (you can install it using pip install django)
* Steps
  * Clone this repository: git clone https://github.com/kjankowitz/FoodForThought.git
  * Navigate to the project directory: cd FoodForThought
  * Create a virtual environment: python -m venv venv
  * Activate the virtual environment:
  * On Windows: venv\Scripts\activate
  * On macOS/Linux: source venv/bin/activate
  * Install project dependencies: pip install -r requirements.txt
  * Run database migrations: python manage.py migrate
  * Start the development server: python manage.py runserver

## Usage
This can be used to collect recipies and gather data on which ones are the most popular.
![First Page](/First_page.png)
![Second Page](/page2.png)
![Third Page](/page3.png)
![Fourth Page](/page4.png)



## Credits and Highlights
Django Documentation: The official Django documentation was incredibly helpful during development 🚀
HyperionDev Bootcamp: The documentation and guidance from this bootcamp was extremely useful 🔥
