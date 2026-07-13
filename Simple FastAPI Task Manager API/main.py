from fastapi import FastAPI

import models

from database import engine

from task import router

# Create database tables if they do not exist
models.Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(

    # Title shown in Swagger UI
    title="Task Manager API",

    # Description shown in Swagger UI
    description="""
## Task Manager API 

This API allows users to manage their daily tasks...

Thank you for using it and have a nice day from Stackly India

""",

    # Custom Swagger URL
    docs_url="/docs.siddarthha",

)

# Include Task Router
app.include_router(router)


