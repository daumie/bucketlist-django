# Bucketlist API and Web_Application

`"Before the day I die I must visit Canada"`. Alot of people have such phrases. This API creates  the foundaton of an  application that will  help track things you want to do before one dies.

## Bucketlist API

According to Merriam-Webster Dictionary, a Bucket List is a list of things that one has not done before but wants to do before dying.

This is an API for an online Bucket List service using Django-Rest_Framework(DRF)

### Endpoints

Bucketlist Api has the following endpoints

| Endpoint | Functionality |
| -------- | ------------- |
| POST /auth/login | Logs a user in |
| POST /auth/register | Register a user |
| POST /bucketlists/ | Create a new bucket list |
| GET /bucketlists/	| List all the created bucket lists |
| GET /bucketlists/<id> | Get single bucket list |
| PUT /bucketlists/<id> | Update this bucket list |
| DELETE /bucketlists/<id> | Delete this single bucket list |
| GET /bucketlists/<id>/items/<item_id> | Get a single bucket list item |
| POST /bucketlists/<id>/items/ | Create a new item in bucket list |
| PUT /bucketlists/<id>/items/<item_id> | Update a bucket list item |