from fastapi import FastAPI 
app = FastAPI()

@app.get('/')
def root():
  return {'message':'hello world'} 

@app.get('/posts')
def get_post():
  return {'data':'this is your posts'}