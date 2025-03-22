from fastapi import FastAPI
import uvicorn  # 需要导入 uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
