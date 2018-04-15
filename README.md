# Student Information System

A command-line interface (CLI) that enables Students, Instructors, Registrars, and Administrators to perform various tasks.

## About

This CLI is written in Python and communicates with a remote MySQL database.  It has a MVC architecure aided by a simple [Router](https://github.com/MatthewKosloski/student-information-system/blob/master/router.py) that enables controllers to communicate with each other and display their views.

## Usage

First, clone the repo:

```
$ git clone https://github.com/MatthewKosloski/student-information-system.git
```

Then, create a virtual environment for the project:

```
$ virtualenv student_information_system
```

Start up the virtual environment (make sure you're in the project's root directory):

```
$ source bin/activate
```

Run the below command to install the packages found in requirements.txt:

```
$ pip install -r requirements.txt
```

Execute the script:

```
$ python app.py
```

## Resources

- [Peewee documentation](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html)