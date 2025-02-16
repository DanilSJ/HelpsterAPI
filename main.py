from fastapi import FastAPI
import uvicorn

from users.views import router as user_router

app = FastAPI(
    title="User Management API",
    description="API HelpsterAPI",
    version="0.1.0"
)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
