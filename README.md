## Backend-Django
In this repository you will find all the information for the Yaus API

## Deployed on heroku
Follow the next link to see the project:

[](https://yaus-api.herokuapp.com/)




## Token Authentication
### We decide use authentication via token for the API Yaus.

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
http GET https://yaus-api.herokuapp.com/api/1.0/user/1/ 'Authorization: Token 4252a2e9761d9e0f9e166ad112af267341ec3129'
```

## How to create new resources?
You can create new users o new shor urls :

### How to create a short url?

Make a POST Request to the next url

```bash
#Example using httpie
http GET https://yaus-api.herokuapp.com/api/1.0/register/new_url/
```

Remember that you must send in the body the params

```
{
    'long_url':'',
    'short_url':'',
    short_url_custom :''
}

```
The custom url is only avaliable for Authenticated users via token.

### How can I know my tokens avaliable?

Send a POST request to the following endpoint
```bash
https://yaus-api.herokuapp.com/api/auth/list_token/
```
Response:
```
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


