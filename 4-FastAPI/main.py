from fastapi import FastAPI # here FastAPI is a class that we are importing from fastapi

app = FastAPI()

@app.get('/')

def index():
    return 'Hello FastAPI'

@app.get('/property/{id}') # if we have 100s of pages for property listings then we have to add path parameters and Also, to make sure the entered id is a integer and not a string we need to specify using : int

def property(id:int):
    return f'This is a property page {id}'

@app.get('/user/{username}')

def username(username):
    return f"[This is the page of a user {username}]"

@app.get('/movies')

def movies():
    return {'Movies list': {'Ranabaali','Jailer 2','The Odyssey'}}

# For documentation we can use server name/docs or servername/redoc --> http://127.0.0.1:8000/redoc or http://127.0.0.1:8000/docs