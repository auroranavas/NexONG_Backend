# Getting started

Follow this guide to setup the project:

### Configure virtual enviroment
- Install virtualenv `pip install virtualenv`
- Create a project directory `mkdir nexong-env`
- Move to env directory with `cd nexong-env`
- Create virtual enviroment `virtualenv venv -p python3.11` or `python -m venv <virtrualenv>`
- Activate virtual enviroment
    - **(MacOS)** with `source venv/bin/activate` 
    - **(Windows)** follow this guide https://linuxhint.com/activate-virtualenv-windows/
> Note: if you are not going to use the app, dont forget to deactivate the virtualenv by simply writing `deactivate`
  
### Clone and install requirements
- Clone NexONG-backend repository `git clone https://github.com/ISPP-G5/NexONG_Backend.git`
- Move to NexOng repo with `cd NexONG_Backend`
- Install project dependencies `pip install -r requirements.txt`

### Migrate the app
- Migrate the app `./manage.py makemigrations` & `./manage.py migrate` or `manage.py makemigrations` & `manage.py migrate`

## Create superuser
- `./manage.py createsuperuser` or `manage.py makemigrations`

### Done! now run the app
### Done! now run the app
- Run the API `./manage.py runserver` or `manage.py runserver`
- Access to the DEMO API on `http://127.0.0.1:8000/demoapi/`
