from fastapi import FastAPI, Form # here FastAPI is a class that we are importing from fastapi
from pydantic import BaseModel,Field,HttpUrl
from typing import List, Set
from uuid import UUID
from datetime import date, datetime, timedelta, time

app = FastAPI()

# Now let us see about POST request
# ******** WE FIRST NEED TO USE PYDANTIC DATA MODEL TO CREATE A POST REQUEST BODY ***********

class Profile(BaseModel):  # This is a simple Pydantic Model and we have used this model in post request below
    name:str
    age:int
    place:str

class Image(BaseModel):

    name:str
    url:HttpUrl #  url:str --> Instead of mentioning the url as str, it is better to mention it as HttpUrl which is imported from Pydantic module

class Product(BaseModel): # This Model will be used inside a function
    name:str
    price:int = Field(gt=0,description="The value should be an integer", examples=[999,99999]) # Here we are adding the metadata, to use metadata need to import Field from Pydantic
    discount:int = Field(default=0,examples=[10])
    discounted_price:int
    tags:Set[str]=Field(default=set(), examples=[['Electronics',"Home APpliances","Electricals"]]) # Here to categorize, tags:List[str]=[] we are using the List (L is in uppercase)-->(this is not regular python list(all smallcase), this is imported from Typing module)
    #Set is used to ensure despite having multiple entries in the set, it will not throw as set won't allow duplicate values.
    image:List[Image] # image:Image --> (If the Product model has multiple images to be used then it is better to use List of Image)Here we are using a nested model, Image is the model that we created above.
    # This nested model is used when we have a complex model, we create it separately and then nest it into an another model, instead of adding attributes.
    #below we are providing the example data, if any other developers look at it, then they will come to know what kind of data to provide

    model_config = {

        "json_schema_extra":{
            "examples":[
                    {           
                    "name": "Samsung",
                    "price": 1000,
                    "discount": 10,
                    "discounted_price": 0,
                    "tags": ["Electronics","Home Appliances"],
                    "image": [
                        {
                        "name": "Iphone-Front_View",
                        "url": "https://exampleimage.com/"
                        }
                    ]
                    }
            ]
        }
    } 

#Deeply nested models below is the Offer model

class Offer(BaseModel):
    name:str
    description:str
    price:float
    product_list:List[Product]

class User(BaseModel):
    name:str
    company:str

#Creating a dummy model for understanding the different Time datatypes as an example

class Event(BaseModel):
    event_id:UUID # UUID is the universal unique identification, it has to be imported from uuid module
    start_date: date
    start_time: datetime
    end_time: datetime
    repeat_time: time
    execute_after: timedelta

#below we are creating the route to create a form for username and the password
@app.post('/login')
def login(username:str=Form(...), password:str=Form(...)):
    return {"username":username, "password":password}

@app.post('/event')
def event(event:Event):
    return {event}

# Here we are creating a route to the Offer model

@app.post('/addoffer')
def addoffer(offer:Offer):
    return {offer}

@app.post('/addproduct/{product_id}') # Here we will pass both path and query parameters
def addproduct(product:Product,product_id:int, category:str):
    product.discounted_price = product.price - (product.price * product.discount/100)
    return {'Product is': product, 'Product_id is': product_id,'It comes under':category}

@app.post('/adduser')
def adduser(profile:Profile):
    return profile

# Now we will work on passing multiple models
@app.post('/purchase')
def purchase(user:User, product:Product):
    return {"User": User, "Product": Product}

#***********************************************************************

@app.get('/') #--> This is called a route
def index():
    return 'Hello FastAPI'

@app.get('/property/{id}') #--> This is called a route # if we have 100s of pages for property listings then we have to add path parameters and Also, to make sure the entered id is a integer and not a string we need to specify using : int
def property(id:int):
    return f'This is a property page {id}'

@app.get('/user/{username}') #--> This is called a route and the username is the path parameter in the above, id is the path parameter
def username(username):
    return f"[This is the page of a user {username}]"

@app.get('/movies') #--> This is called a route
def movies():
    return {'Movies list': {'Ranabaali','Jailer 2','The Odyssey'}}

# For documentation we can use server name/docs or servername/redoc --> http://127.0.0.1:8000/redoc or http://127.0.0.1:8000/docs

@app.get ('/products')
def products(id,price):  # Here id and price are the query parameter and not the path parameter
    return {f'The product id is {id} and the price is : {price}'}  # to use this, the url should be : http://127.0.0.1:8000/products?id=10, need to give '?' and then the parameter and assign value

# To handle multiple query parameters need to use "&" after the first parameter : http://127.0.0.1:8000/products?id=10&price=40

# the below is the example of using both query and path parameters

@app.get('/profile/{userid}/comments/')
def profile(userid:int,commentid : int):
    return {f'The user id is : {userid} and the commentid is: {commentid}'}

@app.get ('/productsdefaultqueryvalues')
def products(id:int=None,price:int=0):  # Here id is the query parameter and not the path parameter
    return {f'The product id is {id} and the price is : {price}'} 




