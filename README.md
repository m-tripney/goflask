# goflask.py

A command line tool for the Mac which creates a (very) basic Flask app. It will ask for a project name and location then, in that location, do the following:

- create a virtual environment (titled `<project name>_venv`)
- upgrade `pip`
- install `Flask`
- optionally install `Black` with flags `-b` or `--black`
- create an `app.py` file with boilerplate code
- create two directories: `static` and `templates`
- export the `FLASK_APP` environment variable (prep for web server)
- optionally export the `FLASK_ENV` environment variable and set to `development` (i.e. debug mode)  with flags `-d` or `--debug`

Root directory entry uses autocompletion — simply TAB through your folders.