# Getting Started with DRF and REACT Integrated Project Boilerplate template

## Available Scripts

Create a project directory

### `mkdir <folder-name>`

### `cd <folder-name>`

<br/>

Now create a virtual environment

### `python -m venv <envname>`

<br/>

Activate the virtual environment

#### For Windows

### `<envname>\Scripts\activate`

#### For Unix or Mac-OS

### `source <envname>/bin/activate`

Install Django first

### `source <envname>/bin/activate`

<br/>

Create new django project

### `django-admin startproject --template https://github.com/phatakp/drf-react-template/archive/master.zip setup .`

Install necessary requirements

### `pip install -r ./requirements.txt'`

<br/>

Update DB details in local settings file.
Run Python migrate

### `python manage.py makemigrations`

### `python manage.py migrate`

<br />

For React - install dependencies

### `npm install`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

### `npm run build`
