# Description

EmeraldBox is a boilerplate framework for developing python web applications with database access. 
The underlying web framework is Flask, a python microframework based on werkzeug, jinja2 and good intentions. 
Flask gives a complete basic package. EmeraldBox gives structure and helper tools to speed up development and app deployment on Google App Engine.
Helper tools are included but still in its initial amount.

The repo is inspired by Blossom's Flask GAE Skeleton but has been improved into using the python2.7 runtime and ndb.
The basic Blossom's skeleton repo is https://github.com/blossom/flask-gae-skeleton.git

# Motivation

People tend to get confused when developing for Google App Engine. Due to the success in developing EmeraldBox for normal web platform, we decided to port it for google App Engine.

In the latest addition, we have added ndbtools which provides autocasting properties when you assign values to float or integer properties as well as value parsers that will help you save a number of lines to be written, resulting in a cleaner and more readable code.

Just like in the basic EmeraldBox, we are standing in the shoulder of giants, leveraging the following technologies and knitting them to work hand-in-hand:
* Twitter Bootstrap
* Flask
* Best of Python Packages

# Installer package

To run EmeraldBox on GAE, you need python 2.7 and Google App Engine SDK

You can add your desired python package from git repo by running:

    ./box.py -a <repo address> <package name>

Your basic template comes with bootstrap to help you worry less about the UX. You can change this to meet your needs.

# Setup
You can get EmeraldBox by cloning this repo:

    git clone https://github.com/femmerling/EmeraldBox-on-GAE.git <project_name>

To get started with EmeraldBox, use terminal and go to the EmeraldBox root folder and run:

    python setup.py <app engine identifier>

The setup will then automatically download packages and adjusted your settings.

If you clone from git and want to control your project using git do the followings:

change to directory of <project_name>

    cd <project_name>

add replace remote

    git remote rm origin
    git remote add origin <new_remote like git@github.com:your_name/project_name.git>
    git commit -am "initial setup"
    git push origin master

# Server and Deployment

EmeraldBox-on-GAE runs on Google App Engine, therefore you will need the sdk which already includes the testing server and uploader to App Engine's production environment.

# Usage

Framework generators and tools available. to see the functions:

    ./box.py -h


Automated database creation tool available.

Run the following:

    ./box.py -n <Model Name> <field name>:<field type>

This will create an automated data management tool for Create, Read, Update and Delete.
You can access the tool at < server_root > / < model name in lowercase >

Check main.py to see the result.

You can also initiate your own controller in the controller file.
Simply run the following

    ./box.py -i <controller name>


this controller initiation will also automatically generate a view file in your app/templates/ folder with your controller name as the file name.

# Other Notes

Currently this is the only documentation available and the project is still developing from day to day. Use carefully!

EmeraldBox is tested only on unix/linux systems and can only run in unix/linux systems.

If you wish to use the regular datastore, please adjust based on https://docs.google.com/document/d/1AefylbadN456_Z7BZOpZEXDq8cR8LYu7QgI7bt5V0Iw/edit?pli=1

for documentation on python see http://www.python.org <br>
for documentation on Flask see http://flask.pocoo.org <br>
for documentation on Google App Engine see https://developers.google.com/appengine/docs/python/gettingstartedpython27/ <br>
for documentation on Google NDB see https://developers.google.com/appengine/docs/python/ndb/ <br>

# Contributing

If you found any issues please put them in the issue section.

To contribute, simply place a pull request and email the author at erich@emfeld.com

# Ending Note

This framework adds the diversity in python, a language which have more web frameworks than keywords.
Thank you for trying it out and all suggestions are welcome.

Also, special thanks to Thomas Schranz, Allan Berger, and Nik Graf for the initial skeleton.