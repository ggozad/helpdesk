import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

SITE_URL = os.environ.get("SITE_URL")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[SITE_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
