# convin_assignment
Tasks report scheduling

# Installation 

## Install the project dependencies

`pip install -r requirements.txt`

## Run the command to generate the database
`python manage.py migrate`

## Generate super user
`python manage.py createsuperuser`

## Run the server
`python manage.py runserver`
* `Admin page :  http://127.0.0.1:8000/admin`
* `Tasks :  http://127.0.0.1:8000/api_task/v1/`
* `Tasks Tracker :  http://127.0.0.1:8000/api_task_tracker/v2/`


### Tasks
* `GET /api_task/v1/{pk}`
* `POST /api_task/v1/{pk}`

### Tasks Trackers
* `GET /api_task_tracker/v2/{pk}`
* `POST /api_task_tracker/v2/{pk}`
