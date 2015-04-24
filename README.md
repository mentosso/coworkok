**CoWorkOk**
# CoWorking - find and rent a desk


### Setup:

1. Clone this repository (`git clone git@github.com:dook/coworkok.git`)

2. Install requirements (`pip install -r requirements.txt`), probably you should use virtualenv for this.

3. Setup database, use postgreSql 9.1+


### What you have to do (tasks with * are not necessary, but welcome):

# Backend:

1. Extend Company model, for example add fields like: NIP, website, company logo (needs for other task).

2. Extend Location model, add: address, postal code etc.

4. Add searching for desk by city.

5. Add geolocation fields and use [PostGIS](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/postgis/) to setup search by location.

6. Make location view more dynamic

7. User should be able to rent a desk

7. User should register before he rent desk.

8. Add filtration so user can choose if he want to see all locations or only one with open desks.


# Frontend:

1. In index.html file there are two h2 elements they have 'index-header' class, modify it so text is centered both verticaly and horizontaly.

2. Arrange single searching result based on below mockup ![alt tag](https://raw.githubusercontent.com/dook/coworkok/master/mockup.jpg)

3*. Create javascript dynamic searching of desks via AngularJS


# Tests:

1. Add unit tests for registration form

2*. Try to use [Selenium](http://www.seleniumhq.org) to test registration flow


### What you shouldn't do:


### Links and tips that will help you:

