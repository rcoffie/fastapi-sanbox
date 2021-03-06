from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import Optional

app = FastAPI()


class Post(BaseModel):
  title: str 
  content: str 
  published: bool = True
  rating: Optional[int] = None

@app.get('/')
def root():
  return {'message':'hello world'} 

@app.get('/posts')
def get_post():
  return {'data':'this is your posts'}


@app.post('/createposts')
def create_posts(new_post:Post):
  print(new_post)
  return {'data':'post added'}
