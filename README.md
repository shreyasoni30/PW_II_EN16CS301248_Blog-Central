# Blog_Central

A blog application developed in Django.

## Posts
![ezgif com-video-to-gif](https://user-images.githubusercontent.com/38559396/55287491-12c4de80-53c7-11e9-8c6a-3f02b79ba9ca.gif)


## Comments
![Peek 2019-10-15 11-41](https://user-images.githubusercontent.com/38559396/66840502-c9fcfd80-ef85-11e9-827c-51fa4064a231.gif)

## Steps to setup Blog Central

### Create virtual enviornment and clone this git repository

```sh

$ virtualenv blogcentral

$ git clone https://github.com/shreyasoni30/PW_II_EN16CS301248_Blog_Central.git

```


### Running the Django development server and setting up dependencies

Activate the virtual environment with the command:

```sh

$ source blogcentral/bin/activate

$ cd myproject

```

To install the necessary requirements, run the following command:

```sh

$ pip install -r requirements.txt

```

To install Django, run the following command:

```sh

$ pip install django

```

Use the following commands to migrate the database and to test run the Django inbuilt development server.

```sh

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver 0.0.0.0:8000

```

Go to the address 

``` http://127.0.0.0:8000/```

#### Creating An Administration Site
We will create an admin panel to create and manage Posts.In order to use the Django admin first, we need to create a superuser by running the following command in the prompt.

```sh

$ python manage.py createsuperuser

```

You will be prompted to enter email, password, and username. Note that for security concerns Password won't be visible.

```sh

Username (leave blank to use 'user'): admin
Email address: admin@gamil.com
Password:
Password (again):

```
Enter any details you can always change them later. After that rerun the development server and go to the address 

```http://127.0.0.1:8000/admin/```


You should see a login page, enter the details you provided for the superuser.

![Django Admin login](https://tutorial.djangogirls.org/en/django_admin/images/login_page2.png)

After logging in with registered superuser you can add posts for the website. You can also change status of each post via editing it and activate comments.




# Contributors
Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.



