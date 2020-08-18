How to install and run our application 
======================================

Welcome! Here's how to install and run our application.

1. Install Git from ``https://git-scm.com/downloads``

2. Install Python from the terminal (We are using Python3)

    **Linux/WSL** ::

        $ sudo apt-get install python3
    
    **Mac**  ::

        $ brew install python3

    .. note:: You need Homebrew to install Python3 for Mac. Paste this into terminal to install Homebrew: ::

        $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"



3. Install package manager pip from the terminal ::

    $ sudo apt install python3-pip

.. note:: If you get an error, try ``$ sudo apt-get update``

4. Install Flask and its extensions ::

    $ pip3 install flask
    $ pip3 install flask-wtf flask-sqlalchemy flask-login


5. Clone our Repository from github (with HTTPS): ::

    https://github.com/cmpe131-spring2020/team4StP.git

6. Go to the project directory

7. Type ``$ python3 run.py`` into the terminal to run the application