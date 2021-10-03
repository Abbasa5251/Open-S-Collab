## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/OpenSCollab/Open-S-Collab.git
```

download the requirements

```sh
$ pip install -r requiments.txt
```

migrate

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

`Note: we're not using a common database that is why you have to migrate and you can test and if you mess up with the database that will not be public you can just delet db.sqlite3 file and run the above commands again `

run

```
$ python manage.py runserver
```

and then navigate to `localhost:8000`
