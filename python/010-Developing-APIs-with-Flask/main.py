import datetime
from typing import Union
from fastapi import FastAPI
import pytz  # Added import for timezone handling
from pydantic import BaseModel

utc_now = datetime.datetime.now(pytz.UTC)  

app = FastAPI()
fake_db = [
    {'title': f'Creating an application with Django', 'date': utc_now, 'published': True},
    {'title': f'Learning about APIs using FastAPI', 'date': utc_now, 'published': True},
    {'title': f'Developing with Flask', 'date': utc_now, 'published': True},
    {'title': f'Integrating React with other technologies', 'date': utc_now, 'published': False},
    {'title': f'Exploring advanced features of Angular', 'date': utc_now, 'published': True}
]  # simulating a database 

class Post(BaseModel):
    def __init__(self, title: str, date: datetime.datetime):
        self.title = title
        self.date = date = date.now(pytz.UTC)
        published: bool = False # default value

@app.post("/posts", status_code=201) 
def create_post(post: Post):
    return post


@app.get("/posts", status_code=200) 
def read_posts(published: bool, skip: int = 0, limit: int = 0) -> Union[list, dict]:
    if published: 
        published_posts = [post for post in fake_db if post['published']]
        return published_posts[skip: skip + limit]  # pagination
    return {"message": "No published posts available."}, 404  

# Routes (or Endpoints)
@app.get("/posts/{framework}", status_code=200) 
def read_framework_posts(framework: str):
    utc_now = datetime.datetime.now(pytz.UTC)  
    return {
        "posts": [
            {'title': f'Creating an application with {framework}', 'date': utc_now},
            {'title': f'Learning about APIs using {framework}', 'date': utc_now},
            {'title': f'Developing with {framework}', 'date': utc_now},
            {'title': f'Integrating {framework} with other technologies', 'date': utc_now},
            {'title': f'Exploring advanced features of {framework}', 'date': utc_now}
        ]
    }

    '''
    route: /posts/django
    response:
    {"posts":[{"title":"Creating an application with django","date":"2026-01-10T13:53:52.750087+00:00"},{"title":"Learning about APIs using django","date":"2026-01-10T13:53:52.750087+00:00"},{"title":"Developing with django","date":"2026-01-10T13:53:52.750087+00:00"},{"title":"Integrating django with other technologies","date":"2026-01-10T13:53:52.750087+00:00"},{"title":"Exploring advanced features of django","date":"2026-01-10T13:53:52.750087+00:00"}]}
    '''

# Required values (e.g., var: bool) must be declared before optional values (e.g., var: bool = True)