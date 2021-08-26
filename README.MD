# RUNNING THE APPLICATION
1. Go to the root directory sayollo_backend_task/
2. Run 'docker compose up'

# DEVELOPMENT WORKFLOW
To improve development workflow, I have created four different working environment albeit not needed for this mini-task. Development, Staging, Production and Testing; the division of which is found on the config.py file.
Each working environment, in real life projects would have its own database server, domain and certain running specifics to avoid messing or deleting production data and to ensure a smooth development process.

# DATABASE MANAGEMENT SYSTEM
The database management system of choice is PostgreSQL with SQLAlchemy as an ORM Mapper. The database is running as a docker container and the connection params are written in the config.py file.
Database tables are created with the help of SQLAlchemy Schema Definition Language as classes and then initialized with the help of the db driver found at app/src/db/driver.py which is called in __init__.py
Considering the delay in database server startup, the application will retry to establish connection upon failure a number of 14 times, the current number of retries holds no particular importance other than give more opportunities to establish connection.

# FRAMEWORK
I chose Flask as it is a lightweight framework, but gives us the ability to scale depending on the application needs. It also has a lot of modules, which makes the development process quite faster. 
One of the core modules I like to use when it comes to REST APIs in Flask, is Flask-Restx. This module provides tools for the best interaction with the api we build, and also gives us the ability to document our API in Swagger, which is also the tool I use to test my APIs together with Postman.

# ARCHITECTURE
For organization purposes, I am making use of Namespaces to create Api endpoints. Currently there are two endpoints:
1. /getAd
2. /impressions

Both of which use the POST HTTP Method requiring the following parameters to be sent as json:
{
  "sdk_version": "string",
  "session_id": "string",
  "platform": "string",
  "user_name": "string",
  "country_code": "string"
}

# PROCESS
After running the application, visit http://localhost:5000/api/ to see the Swagger Documentation

### Making a request on /getAd
   If JSON parameters are sent incorrectly, the response code will be 400. 
   If the JSON parameters on request are sent correctly, then a request will be make to receive a VAST XML, and the JSON data will be stored in the database. 
   #### Storing the data in the database
   Ad requests per SDK Version and Ad requests per Username are stored in two different tables, ad_requests_by_sdk and ad_requests_by_user respectively. 
   To save an ad request per SDK Version/Username, first we query on the table to see if that SDK Version/Username exists on the table, if yes, we increment the ad_request column by one. Else, if the record does not exist on the table, we insert a row with that SDK Version /or Username and ad_request value set to 1.

### Making a request on /impressions
   If JSON parameters are sent incorrectly, the response code will be 400. 
   If the JSON parameters on request are sent correctly, then the JSON data will be stored in the database. 
   #### Storing the data in the database
   Impressions per SDK Version and Impressions per Username are stored in two different tables, impressions_by_sdk and impressions_by_user respectively. 
   To save an impression per SDK Version/Username, first we query on the table to see if that SDK Version/Username exists on the table, if yes, we increment the impressions column by one. Else, if the record does not exist on the table, we insert a row with that SDK Version /or Username and impressions value set to 1.

