# jkfc_project
Participants: Jonne Saajos, Jere Mustikkamaa and Jukka Virkkula

# Venv
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Luominen
#### On linux
    python3 -m venv venv
    
#### On windows
    py -m venv env

## Aktivointi

#### On Linux
    cd projektikansio
    source venv/bin/activate
#### On Windows
    cd projektikansio
    source venv\Scripts\activate
    
## Pakettien asentaminen
    (venv) pip install <paketti>
    (venv) pip freeze > requirements.txt
    
## Venvin uudelleenluominen

#### On linux
    python3 -m venv venv
    source venv/bin/activate
    (venv) pip install -r requirements.txt
#### On windows
    py -m venv venv
    source venv/Scripts/activate
    (venv) pip install -r requirements.txt

## Projektin luonti
    django-admin startproject kuvagalleria
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py startapp <app>

## Site map
### `/`
```
Displays public photogallery page
```
### `/upload`
```
Image upload page
```
### `/search/?search=<search-term>`
```
Searches images by title
```
### `/profile/<username>`
```
Displays all user's images
```
### `images/<image_id>/`
```
Displays photoview
```
