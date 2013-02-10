# fogfudge.com

*  This a the production site for fogfudge.com and also a fully portable example of Mezzanine with Cartridge shopping cart plugin.
*  Uses venv for application distribution.
*  Tested deployable to heroku.
*  Includes some sample data.
*  Follow the commits to see my modifications one at a time.
*  I did one commit at first that held several changes (my bad).

## Installing
* `git clone git@github.com:clickyspinny/fogfudge.git`
* `cd fogfudge`
* demo database setup
    * `cp local_settings.py.example local_settings.py`
    * production database (set in settings.py) is configured for use with heroku
* key setup
    * change the SECRET_KEY value in settings_secret_key.py.example to something totally different
    * `cp settings_secret_key.py.example settings_secret_key.py`
* optional setup
    * change values in settings_mail.py.example then 
    * `cp settings_mail.py.example settings_mail.py`
* `virtualenv venv --distribute`
* `. venv/bin/activate`
* `pip install -r requirements.txt`
* `deactivate` turn off venv (optional)

## Running Locally
* go to fogfudge dir `cd MYPATH/fogfudge`
* `. venv/bin/activate`
* ./manage.py runserver
* open up web browser to local site: http://127.0.0.1:8000
* or http://127.0.0.1:8000/admin login: admin/admin

## Heroku

### Deployment
*  Create new app on heroku `heroku create`
*  Rename it `heroku apps:rename newname`
*  deploy `git push heroku master`
*  ref: https://devcenter.heroku.com/articles/django

### Files that have been modified for heroku, fyi
* configured for the heroku (postgres) database via https://github.com/clickyspinny/fogfudge/blob/master/settings.py#L219
* configured for heroku served static files
    * urls.py - https://github.com/clickyspinny/fogfudge/blob/master/urls.py#L15
    * Procfile -  https://github.com/clickyspinny/fogfudge/blob/master/Procfile#L1
    * settings.py - https://github.com/clickyspinny/fogfudge/blob/master/settings.py#L317
* ref: https://gist.github.com/joshfinnie/4046138
