# fogfudge

*  This a the production site for fogfudge.com and also a fully portable example of Mezzanine with Cartridge shopping cart plugin.
*  Uses venv for application distribution.
*  Tested deployable to heroku.
*  Includes some sample data.
*  Follow the commits to see my modifications one at a time.
*  I did one commit at first that held several changes (my bad).

## Installing
* `git clone git@github.com:clickyspinny/fogfudge.git`
* `cd fogfudge`
* `virtualenv venv --distribute`
* `. venv/bin/activate`
* `pip install -r requirements.txt`
* `deactivate` turn off venv (optional)

## Running
* go to fogfudge dir `cd MYPATH/fogfudge`
* `. venv/bin/activate`
* ./manage.py runserver
* Open up web browser to local site: http://127.0.0.1:8000
