# Student Information System

A command-line interface (CLI) that enables Students, Instructors, Registrars, and Administrators to perform various tasks.

## About

This CLI is written in Python and communicates with a remote MySQL database. It has a MVC architecure aided by a simple [Router](https://github.com/MatthewKosloski/student-information-system/blob/master/router.py) that enables controllers to communicate with each other and display their views.

## Usage

First, clone the repo:

```
$ git clone https://github.com/MatthewKosloski/student-information-system.git
```

Then, create a virtual environment for the project (make sure you're in the project's root directory):

```
$ virtualenv student-information-system
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

## Installing Packages

After you install a package via Pip, please save it to requirements.txt like so:

```
$ pip freeze > requirements.txt
```

## Resources

* [Peewee documentation](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html)
* [Peewee Fields](http://docs.peewee-orm.com/en/latest/peewee/models.html#fields)

## Notes

Peewee doesn't support an ENUM type, so we must use integers instead.

The `letter_grade` column in the `registration` table takes the following integers:

* 1 (A)
* 2 (B)
* 3 (C)
* 4 (D)
* 5 (F)

The `meet_day` column in the `section` table takes the following integers:

* 1 (M)
* 2 (T)
* 3 (W)
* 4 (R)
* 5 (F)
* 6 (MWF)
* 7 (TR)

The `type` column in the `section` table takes the following integers:

* 1 (lecture)
* 2 (online)
