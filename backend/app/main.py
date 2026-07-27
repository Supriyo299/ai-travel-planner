from fastapi import FastAPI

app = FastAPI(
    title="AI Travel Planner API",
    version="1.0.0",
    description ="API for planning travel itineraries"
)

@app.get("/")
def read_root():
    return {"message": "AI Travel Planner API is running."}
