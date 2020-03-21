## Backend onboarding project

A simple Order/ Transaction management system.

Purpose — to introduce and familiarise you to the basic tenets of a highly
scalable, web-based application (from the POV of UrbanPiper :)) 

So, what are we building? 

• A simple transactional system

• Comprises of:
 - Items (name, price, description)
 - Stores (name, address, lat, lng)

• Orders/ Transactions: 
 - Made up of items
 - Each order is associated w/ a single store and merchant
 - Orders can be placed only when the store, items and order are all associated with the same merchant
 
 
## Getting started

Steps:

1. **Clone the project** and change directory into the cloned folder
2. **Install pyenv** [link](https://github.com/pyenv/pyenv#homebrew-on-macos) .This will seperate your system's python installation, from what's required by the project. This project required python version `3.6.5`. 
      * Install python version 3.6.5 in pyenv and set it as the local python env
3. **Install mysqlv5.7** This project uses mysql `5.7`, follow the steps below after installation,
      * `mysql_config` must be installed, if this is not installed the next step will fail
      ```sudo apt-get install libmysqlclient-dev```[link to stackoverflow](https://stackoverflow.com/questions/7475223/mysql-config-not-found-when-installing-mysqldb-python-interface)
      * Create a database called updjango_db
      * Create a new user and grant all the permissions to this db and configure the username and password in `settings.py`
4. **Create a virtual env** and Install the dependencies in the requirements.txt file
5. **Installing rabbitmq** Install the latest version of rabbitmq
      * Rabbitmq depends on erlang and might throw an error during installations because of an incompatable versions. 
      This stackoverflow link to install the correct version of erlang helps [link](https://stackoverflow.com/questions/44685813/how-do-i-install-a-specific-version-of-erlang)
      * Start the rabbitmq server in the background
6. **Run Migrations** Make migrations and migrate the project, create a super user to use the django admin portal
7. **Start Server** Run the server, the server will be running at http://localhost:8000

## API Docs

This project uses JWT for authentication, all requests other than login and request token must contain 
The header `Authorization`:`Bearer TOKEN_FROM_REFRESH_TOKEN_RESPONSE`

### Login - Get the JWT token

URL - `/api/token/`

request body 
```json
  {
	 "username":"YOUR_USERNAME",
	 "password":"YOUR_PASSWORD"
  }
```

A succesful response, contains an Access token that is valid for 5 minutes and a refresh token which can be used to 
get a token with a validitiy of 24 hours

response body
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NDkxNzk2OCwianRpIjoiNjNmYmE1ZjBhODcxNDQ3YmIyMjExY2ZmNzkwZTcwN2EiLCJ1c2VyX2lkIjoxfQ.oZ6R8lAUN_ubtGFEPqnCxyNhwUFnoe8vJOitWN-1VpU",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg0ODMxODY4LCJqdGkiOiJhMzA4ZTk0YzA0MDg0NTA5OGMwNzNjODdmMmEzY2VhOSIsInVzZXJfaWQiOjF9.kETgnqchKS3kS1YQ7hcsrBwb8BT04WEGX8zFaqlYljg"
}

```


### Refresh token 

URL - `/api/token/refresh/`

request body 
```json
{
	"refresh":"REFRESH_TOKEN_FROM_LOGIN_RESPOSE"
}
```

A succesful response, contains an Access token that is valid for 24 hours

response body
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg0ODE3ODkzLCJqdGkiOiI3YmQxYmEwNzMzYWQ0MTBhODkwYmE3YTcwMDE5OGNlMiIsInVzZXJfaWQiOjF9.TBHZWhs8JlggC-97maurqb8Nz-vfwsV7zHmUqmLdUCQ"
}

```

### Merchant

#### GET

URL - `/api/merchants/` - Returns a list of all merchants


response body 
```json
[
    {
        "id": 1,
        "name": "Chai Point",
        "owner": 1
    }
]
```

URL - `/api/merchants/<int:pk>/` - Returns the merchant detail for a specific merchant


response body 
```json
{
   "id": 1,
   "name": "Chai Point",
   "owner": 1
}
```

#### POST
URL - `/api/merchants/` - Add a new merchant

request body 
```json
{
    "name": "Kanti sweets",
    "owner": 1
}
```

response body
```json
{
    "message": "merchant saved"
}
```

#### PUT 
URL - `/api/merchants/<int:pk>/` - Edit a merchant

request body 
```json
{
    "name": "Kanti sweets",
    "owner": 1
}
```

response body
```json
{
    "message": "merchant saved"
}
```
#### DELETE
URL - `/api/merchants/<int:pk>/` - delete a merchant

response status - 204 no content


### Store
#### GET

URL - `/api/stores/` - Returns a list of all stores


response body 
```json
[
    {
        "id": 1,
        "name": "Nallurhalli",
        "address": "Brigade irv center",
        "lat": 12.12345,
        "lng": 12.21356,
        "merchant": {
            "id": 1,
            "name": "Chai Point",
            "owner": 1
        }
    }
]
```

URL - `/api/store/<int:pk>/` - Returns the store detail for a specific merchant


response body 
```json
{
    "id": 1,
    "name": "Nallurhalli",
    "address": "Brigade irv center",
    "lat": 12.12345,
    "lng": 12.21356,
    "merchant": {
       "id": 1,
       "name": "Chai Point",
       "owner": 1
    }
}
```

#### POST
URL - `/api/stores/` - Add a new store

request body 
```json
{
   {		
     "name": "Cunningham Road",
     "address": "Super, cunning",
     "lat": 45.9699,
     "lng": 24.7319,
     "merchant": {
        "id": 1,
        "name": "Chai Point",
        "owner": 1
     }
   }
}
```

response body
```json
{
    "message": "Store saved"
}
```

#### PUT 
URL - `/api/merchants/<int:pk>/` - Edit a Store

request body 
```json
{
   {		
     "name": "Cunningham Road",
     "address": "Super, cunning",
     "lat": 45.9699,
     "lng": 24.7319,
     "merchant": {
        "id": 1,
        "name": "Chai Point",
        "owner": 1
     }
   }
}
```

response body
```json
{
    "message": "Store edited successfully"
}
```
#### DELETE
URL - `/api/stores/<int:pk>/` - delete a store

response status - 204 no content


### Item

#### GET

URL - `/api/items/` - Returns a list of all items


response body 
```json
[
    {
        "id": 1,
        "name": "Vada Pav",
        "price": "25",
        "description": "Mumbai style",
        "merchant": {
            "id": 1,
            "name": "Chai Point",
            "owner": 1
        }
    }
]
```

URL - `/api/items/<int:pk>/` - Returns the item detail for a specific merchant


response body 
```json
{
    "id": 1,
    "name": "Vada Pav",
    "price": "25",
    "description": "Mumbai style",
    "merchant": {
        "id": 1,
        "name": "Chai Point",
        "owner": 1
    }
}
```

#### POST
URL - `/api/items/` - Add a new item

request body 
```json
{
    "name": "Egg Puff",
    "price": "25",
    "description": "An assortment of vegetables wrapped in a flaky pastry, baked to perfection",
     "merchant": {
        "id": 1,
        "name": "Chai Point",
        "owner": 1
    }
}
```

response body
```json
{
    "message": "merchant saved"
}
```

#### PUT 
URL - `/api/items/<int:pk>/` - Edit an item

request body 
```json
{
    "name": "Egg Puff",
    "price": "25",
    "description": "An assortment of vegetables wrapped in a flaky pastry, baked to perfection",
     "merchant": {
        "id": 1,
        "name": "Chai Point",
        "owner": 1
    }
}
```

response body
```json
{
    "message": "merchant saved"
}
```
#### DELETE
URL - `/api/items/<int:pk>/` - delete an item

response status - 204 no content


### Order

#### GET
URL - `/api/orders/` - Returns a list of all order

response body 
```json
[
    {
        "id": 1,
        "address": "Celery shared task 1",
        "merchant": {
            "id": 1,
            "name": "Chai Point",
            "owner": 1
        },
        "store": {
            "id": 1,
            "name": "Nallurhalli",
            "address": "Brigade irv center",
            "lat": 12.12345,
            "lng": 12.21356,
            "merchant": {
                "id": 1,
                "name": "Chai Point",
                "owner": 1
            }
        },
        "items": [
            {
                "id": 1,
                "name": "Vada Pav",
                "price": "25",
                "description": "Mumbai style",
                "merchant": {
                    "id": 1,
                    "name": "Chai Point",
                    "owner": 1
                }
            }
        ],
        "order_subtotal": 234.0,
        "taxes": 123.0,
        "order_total": 123.0,
        "created_time": "2020-03-21T21:03:22.428609Z",
        "delivery_time": "2020-03-21T21:43:16.446742Z"
    },
    {
        "id": 2,
        "address": "Celery shared task 1",
        "merchant": {
            "id": 1,
            "name": "Chai Point",
            "owner": 1
        },
        "store": {
            "id": 1,
            "name": "Nallurhalli",
            "address": "Brigade irv center",
            "lat": 12.12345,
            "lng": 12.21356,
            "merchant": {
                "id": 1,
                "name": "Chai Point",
                "owner": 1
            }
        },
        "items": [
            {
                "id": 1,
                "name": "Vada Pav",
                "price": "25",
                "description": "Mumbai style",
                "merchant": {
                    "id": 1,
                    "name": "Chai Point",
                    "owner": 1
                }
            }
        ],
        "order_subtotal": 234.0,
        "taxes": 123.0,
        "order_total": 123.0,
        "created_time": "2020-03-21T22:08:21.396133Z",
        "delivery_time": "2020-03-21T22:52:01.217416Z"
    }
]
```

URL - `/api/orders/<int:pk>` - Returns the details for a single order
response body
```json
{
    "id": 1,
    "address": "Celery shared task 1",
    "merchant": {
        "id": 1,
        "name": "Chai Point",
        "owner": 1
    },
    "store": {
        "id": 1,
        "name": "Nallurhalli",
        "address": "Brigade irv center",
        "lat": 12.12345,
        "lng": 12.21356,
        "merchant": {
            "id": 1,
            "name": "Chai Point",
            "owner": 1
        }
    },
    "items": [
        {
            "id": 1,
            "name": "Vada Pav",
            "price": "25",
            "description": "Mumbai style",
            "merchant": {
                "id": 1,
                "name": "Chai Point",
                "owner": 1
            }
        }
    ],
    "order_subtotal": 234.0,
    "taxes": 123.0,
    "order_total": 123.0,
    "created_time": "2020-03-21T21:03:22.428609Z",
    "delivery_time": "2020-03-21T21:43:16.446742Z"
}
```

#### POST
URL - `/api/orders/` - Create a new order

request body 
```json
{
    "address": "Nallurhalli",
    "merchant":{
        "id": 1,
        "name": "Chai Point",
        "owner": 1
    },
    "store": {
        "id": 1,
        "name": "Nallurhalli",
        "address": "Brigade irv center",
        "lat": 12.12345,
        "lng": 12.21356,
        "merchant": {
            "id": 1,
            "name": "Chai Point",
            "owner": 1
        }
    },
    "items": [
        {
        "id": 1,
        "name": "Vada Pav",
        "price": "25",
        "description": "Mumbai style",
        "merchant": {
            "id": 1,
            "name": "Chai Point",
            "owner": 1
            }
        }
    ],
    "order_subtotal": 234.0,
    "taxes": 123.0,
    "order_total": 123.0
}
```

response body

```json 
    "message": "Order Queued"
```



