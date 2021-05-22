import uvicorn
from dotenv import load_dotenv

from factory import app

load_dotenv()
app = app

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
