## Working with FastAPI

FastAPI is a super fast Python framework that allows developers to build APIs. To serve the API it uses Uvicorn which is a fast ASGI-server. While working on this repo, I was able to learn about ways to interact with the API using SwaggerUI which is built within the FastAPI framework.

The API is focused around building a database of users who are admins and students. I was able to use HTTP Request to "GET","POST", "PUT", "DELETE" to interact with the datbase as well. 



### Installing FastAPI
pip install fastapi
pip install uvicorn



### Using FastAPI
In the terminal type the following: uvicorn main:app --reload
(This allows fast reload of any changes made to the API)

To visit the SwaggerUI be sure to place "/docs" at the end of the localhost URL.





