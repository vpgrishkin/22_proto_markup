# Suppliers in Novosibirsk
The [site](vpgrishkin.github.io/22_proto_markup/site/index.html) is an examble using Bootstrap framwork, Jinja2 (templating language) and contains two pages. It been validated by the W3C Validator.

# How to generate html from templates
``` #!bash

virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python render_templates.py
```
Get the result in the folder: site.
# How to change
Use livereload (waching the templates changes):
``` #!bash

python watch_teml.py
```
and get the result: [127.0.0.1:5500](http://127.0.0.1:5500/) 

# Project Goals
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

