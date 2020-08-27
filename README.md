## Backend-Django
In this repository you will find all the information for the Yaus API

## Deployed on heroku
Follow the next link to see the project:

[](https://yaus-api.herokuapp.com/)

## Token Authentication
### We decide use authentication via token for the API Yaus.

### How to generate a token?

Send request via POST including username and pasword to this endpoint

```bash
#Example using httpie: 
http POST https://yaus-api.herokuapp.com/api-token-auth/ username='username' password='password'

#Example of response:

{
    "token": "423332e9761d9e0f9e166ad112af267341ec3129",
    "user_id": 2,
    "email": "user@email.com"
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


#### How to create a new user?

Make a POST request to the next url

```bash
#Example using httpie
http GET https://yaus-api.herokuapp.com/api/1.0/register/user/
```

Remember that you must send in the body the params

```
{
    "username":"example.username",
    "password":"123",
    "first_name":"example",
    "last_name":"example last name",
    "email":"email@email.com"
}

```