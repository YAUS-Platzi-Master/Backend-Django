# Yaus Project - API Repository

> In this repository you will find the documentation about the API behind the YAUS Project

> Yaus is a website that allows you to shorten urls, capture statistics, register / log users, among others

# Table of Contents

- [Installation](#Installation)
- [Deploy](#Deploy)
- [Features](#Features)
- [Documentation](#Documentation)
- [Team](#Team)



# Installation

- All the API is build in python

### Clone

- Clone this repo to your local machine using `git@github.com:YAUS-Platzi-Master/Backend-Django.git`

### Should look like this:

```shell
├── Dockerfile
├── Procfile
├── README.md
├── YAUS
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── throttles.py
│   ├── urls.py
│   └── views.py
├── api_analytics
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── mixins.py
│   ├── models.py
│   ├── serializers.py
│   └── tests.py
├── authKnox
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── staticfiles
│   └── base.html
```

### Config Enviorment variables
Configure these enviorment variables:
- DEBUG: False in production enviorments
- DATABASE_URL: Parse database connection url strings  <a href="https://django-environ.readthedocs.io/en/latest/#environ-env" target="_blank">More Info</a>
- SECRET_KEY: Random key for Django. You can use the command `openssl rand -base64 32` in command line as key generator


```shell
#Example
DEBUG=True
DATABASE_URL=psql://urser:un-githubbedpassword@127.0.0.1:8458/database
SECRET_KEY=ndds9!(0@qr!g^8$4ifcbnyiaumlx^(1q!62ko#s6d12ts2eqj

```

### Setup Docker
Initialize docker container:

```shell
docker-compose run web python manage.py migrate
```

```shell
docker-compose up
```


# Deploy
We user Heroku to deploy the app, tou can look in the following link:
<a href="https://yaus-api.herokuapp.com/api/1.0/register/new_url" target="_blank">https://yaus-api.herokuapp.com/api/1.0/register/new_url</a>

# Features

## Token Authentication
We decide use authentication via token for the API Yaus.

### How to generate a token?

The user must login sending a POST request. 
Remember send the credentials in the body

```bash
#Example
http POST https://yaus-api.herokuapp.com/auth/login/ username='username' password='password'

#Example of response:

{
    "expiry": "2020-08-30T00:06:17.173405Z",
    "token": "c6d7e16ce7432d8aee0cc902d89aae34d8633011e81d7ffe20200bbb175fdd6e",
    "user": {
        "username": "admin"
    },
    "headers": {
        "user_agent": "PostmanRuntime/7.26.3",
        "Host": "localhost:8000"
    }
}
```

### How to use the token?

In the requests add to headers the token like this:

```bash
#Example using httpie
http GET https://yaus-api.herokuapp.com/api/1.0/user/ 'Authorization: Token fbdb01f7da9d1da5be07bdb496f27701cbb1ac4b8073ad325f8fb794cc045105'
```

## How to create new resources?
You can create new users o new shor urls :

### How to create a short url?

Make a POST Request to the next url

```bash
https://yaus-api.herokuapp.com/api/1.0/register/new_url/
```

Remember that you must send in the body the params
- long_url: string of long url that you want to short
- custom_url: boolean value. True if you want to make your custom url. This feature ins avaliable only if you are authenticated
- short_url_custom: string for custom url. Only accept number, letters and/or guion. 

```bash
#Example of body params in requets
{
    'long_url':'https://www.facebook.com/myprofile',
    'custom_url: true,
    'short_url_custom': 'mypr'
}

```
The custom url is only avaliable for Authenticated users via token.

```bash
#Example of response
{
    "Response": "Register new custom url for authenticated User",
    "register_set": {
        "id": 1550,
        "status": "Active",
        "long_url": "http://www.platzi.com/master",
        "short_url": "mycustom3",
        "created": "2020-09-11T04:27:38.132150Z",
        "total_hits": 0,
        "hits": []
    }
}

```

## How to know my resources?

### How to know my user details?
Send a get request to the endpoint

```bash
http://yaus-api.herokuap.com/api/1.0/user

#Example of response
{
    "Response": "User details",
    "data": [
        {
            "id": 2,
            "first_name": "name",
            "last_name": "last_name",
            "username": "name.last",
            "email": "example@yaus.com"
        }
    ]
}
```

### How to know my sets of urls in the system?
Send a get request to the endpoint

```bash
http://yaus-api.herokuap.com/api/1.0/set_of_urls

#Example of response
"Response": "Sets of Urls for user",
    "user": "name.last",
    "total_set_urls": 2,
    "data": [
        {
            "id": 5,
            "status": "Active",
            "long_url": "https://www.instagram.com/profile/myprofile",
            "short_url": "ig-and.and",
            "created": "2020-08-23T05:12:06.271940Z",
            "total_hits": 2,
            "hits": [
                "http://yaus-api.herokuap.com/api/1.0/hits/4/",
                "http://yaus-api.herokuap.com/api/1.0/hits/3/"
            ]
        },
        {
            "id": 2,
            "status": "Active",
            "long_url": "https://www.facebook.com/profile/andres.andrade",
            "short_url": "fb-and.and",
            "created": "2020-08-22T23:27:47.465576Z",
            "total_hits": 0,
            "hits": []
        }
    ]
}
```

If you want to read a set of url determined, you must add de id of the set in th url

```bash
http://yaus-api.herokuap.com/api/1.0/set_of_urls/{id}

#Example

#Get request to:
http://yaus-api.herokuap.com/api/1.0/set_of_urls/2/

    {
        "id": 2,
        "status": "Active",
        "long_url": "https://www.facebook.com/profile/andres.andrade",
        "short_url": "fb-and.and",
        "created": "2020-08-22T23:27:47.465576Z",
        "total_hits": 0,
        "hits": []
    }

```


### How to know my hits?

To know all the hits for my user send a get request like:
```bash
#Get request to:
http://yaus-api.herokuap.com/api/1.0/hits/


#Example of response
{
    "Response": "Hits for user",
    "user": "example user",
    "total_hits_per_user": 2,
    "data": [
        {
            "http_reffer": "https://www.some-ad.com/",
            "ip": "0.0.0.0",
            "country_code": "8",
            "region_code": "8",
            "city": "8",
            "latitude": "0 0 0 0",
            "longitude": "0 0 0 0",
            "agent_client": "Agent",
            "created": "2020-08-25T05:02:09.149385Z",
            "id": 4
        },
        {
            "http_reffer": "https://www.someblog.com/",
            "ip": "0.0.0.0",
            "country_code": "2",
            "region_code": "2",
            "city": "2",
            "latitude": "0 00 0 0",
            "longitude": "0 0 0 0 0",
            "agent_client": "agentclient",
            "created": "2020-08-25T05:01:19.082817Z",
            "id": 3
        }
    ]
}
```


If you want to read a hit determined, you must add de id of the hit in the url

```bash
http://yaus-api.herokuap.com/api/1.0/hit/{id}

#Example

#Get request to:
http://yaus-api.herokuap.com/api/1.0/hit/2/

{
    "http_reffer": "https://www.some-ad.com/",
    "ip": "0.0.0.0",
    "country_code": "8",
    "region_code": "8",
    "city": "8",
    "latitude": "0 0 0 0",
    "longitude": "0 0 0 0",
    "agent_client": "Agent",
    "created": "2020-08-25T05:02:09.149385Z",
    "id": 4
}

```

### How can I know my tokens avaliable?

Send a POST request to the following endpoint
```bash
https://yaus-api.herokuapp.com/api/auth/list_token/
```
Response:
```bash
{
    "username": "admin",
    "count": 1,
    "tokens": [
        {
            "user": 1,
            "token_key": "bbc73e50",
            "created": "2020-08-29T22:57:31.903394Z",
            "expiry": "2020-08-29T23:57:31.903110Z",
            "token_profile": " localhost:8000 : PostmanRuntime/7.26.3"
        }
    ]
}
```

#### How to create a new user?

Make a POST request to the next url

```bash
#Example using httpie
http GET https://yaus-api.herokuapp.com/api/1.0/register/user/
```

Remember that you must send in the body the params

```bash
{
    "username":"example.username",
    "password":"123",
    "first_name":"example",
    "last_name":"example last name",
    "email":"email@email.com"
}

#Response:
{
    "Response": "User created succesfully",
    "username": "example5.username",
    "email": "email3@email.com"
}
```


## How we handle the number of requests?
Depending on the role in the system, the allowed requests are calculated

### Anonymous Users

Anonymous users have limited access to the API.
It is allowed to create a short url per day and it is not possible to consult any related statistics

### Authenticated Users

Authenticated users have greater access to the API, they can create up to 10 short_urls per minute and consult any statistics without exceeding a maximum of 100 requests per minute.

Additionally, the use of the API for developers is allowed, in which case they can create up to 100 shor_urls per minute


# Documentation
You can see more about the documentation <a href="https://documenter.getpostman.com/view/12460085/TVCcYA1E" target="_blank">here</a> 

# About the Team

You can see more about the team <a href="https://www.notion.so/About-us-17978bd2685642aa96778d13bf098d1f" target="_blank">here</a> 
