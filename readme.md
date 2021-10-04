## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/OpenSCollab/Open-S-Collab.git
```

then cd into the project folder and then cd into the folder in which manage.py is there:
```sh
$ cd Open-S-Collab
$ cd open-s-collab
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


### About

***This Project is ane [open source](https://opensource.com/resources/what-open-source) project so anyone can contribute to this project unless he is within the boundaries of the guidelines and rules of this project***

*This project is founded by [akzain](https://github.com/akzain) and [MidouWebDev](https://github.com/midouwebdev)*

This is a project that is built to help the people who want to start an open source porject. Generally open source project needs different kinds of platforms like:

* a chatting app to talk and discuss with their fellow devs.
* a version control app in which github is mostly used
* a video calling app like skype although discords also have the ability to attend a call or a meeting.
* a task managing app like jira

so [akzain](https://github.com/akzain) came up with the idea of have a wesite or an app that could do all the above things except for version control as [github](https://github.com) is irreplaceable

### Tools and stacks we are using
for our backend we'll be uisng [django](https://djangoproject.com) and to build our api we are using [djangorestframework(drf)](https://www.django-rest-framework.org/)

as for our frontend we will be using [reactjs](https://reactjs.org) and will also make a vue version of frontend as well.

Join our [discord sever](https://discord.gg/us9mHJ7K) to talk with our community and get to know more about Open-S-Collab