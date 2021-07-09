from fastapi import FastAPI
from config.database import make_database
from routers import routers


def create_application() -> FastAPI:
    application = FastAPI(
        title="API"
    )

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    print("Starting Up ... ")
    print("Initialize Database ...")
    make_database(app)
    print("Database Succefully Created ... ")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting Down ... ")


@app.get("/")
def index():
    return {
        "details": "index"
    }


for router in routers:
    app.include_router(router)