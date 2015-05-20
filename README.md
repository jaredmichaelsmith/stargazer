Stargazer
==========

Version: 0.1.0
Website: NULL
Authors: Jared Smith, Joseph Connor, Luke Wegryn
Contact: jaredsmi@cisco.com

###Overview:
Stargazer is a tool that recieves a hostname on the command line interface (CLI) and attempts to 
find and map out any REST API's on the hostname. With this mapping, a nice report is generated of
all the endpoints and a concise description of each.

###Installation:
Currently, the tool is NOT available to install with pip. This will be added in the future.

###Usage:
- Runs with Python 2.7.x
- Getting started on Mac OS X and Linux based distributions (Ubuntu/Debian/Arch/etc):
    - `virtualenv venv && source venv/bin/activate` -- Make a virtual environment (Use virtualenv people!) and activate it.
    - `pip install -r requirements.text` -- Install dependencies.
    - `python mapper.py -h` -- Detail of the CLI.
- When you're done:
    - `deactivate` -- Deactivate the virtual environment.

###TODO:
- New name for the project/tool
- Create pip package for the project

