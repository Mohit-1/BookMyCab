# BookMyCab

A simple RESTful implementation to book cabs.

### Pre-requisites - 
Python 3.7.0 or higher

OS - Windows

### Installation instructions - 

1. Clone the repository

2. Install 'virtualenv' to create a virtual environment for our API

   `pip install virtualenv`

3. Setup the virtual environment

   `virtualenv sample_name_for_virtual_env`

4. Activate the virtual environment

   `sample_name_for_virtual_env\Scripts\activate`

5. Install the dependencies

   `pip install -r requirements.txt`

6. Set up the database (first change to the BookMyCab directory)

   `python manage.py makemigrations`


   `python manage.py migrate`

7. Create a superuser

   `python manage.py createsuperuser`

8. Run the server (on localhost:8000)

   `python manage.py runserver`

### API reference - 

**End point** - api/v1/users

**Methods allowed** - GET, POST, HEAD, OPTIONS

       Returns the list of all active users on the platform.



**End point** - api/v1/user/1/

**Methods allowed** - GET, PUT, PATCH, DELETE, HEAD, OPTIONS

      Retrieves information about a particular user.



**End point** - api/v1/cabs

**Methods allowed** - GET, POST, HEAD, OPTIONS

       Returns the list of all active cabs present on the platform.



**End point** - api/v1/cab/1/

**Methods allowed** - GET, PUT, PATCH, DELETE, HEAD, OPTIONS

      Retrieves information about a particular cab.



**End point** - api/v1/book

**Methods allowed** - POST, OPTIONS

**Request parameters** - "cab", "user" (Pass the primary keys for the cab and the user booking that cab)

       Books a cab for a user, if the cab is available.



**End point** - api/v1/history/2/

**Methods allowed** - GET, HEAD, OPTIONS

      Retrieves the booking history for a user or travel history for a driver.
