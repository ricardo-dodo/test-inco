from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, routes
from .database import engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create tables
try:
    models.Base.metadata.create_all(bind=engine)
    logger.info("Successfully created database tables")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")
    raise

app = FastAPI(
    title="Employee Maintenance API",
    description="API for managing employee records",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(routes.router, prefix="/api/v1", tags=["employees"])

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to Employee Maintenance API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080)