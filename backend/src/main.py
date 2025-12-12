from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import dataset_router
from src.routers import basic_visuals


app = FastAPI(title="AI Data Visualization Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later replace with frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dataset_router.router)
app.include_router(basic_visuals.router)


@app.get("/")
def root():
    return {"message": "Backend is running!"}
