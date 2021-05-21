import uvicorn

from factory import app

app = app

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
