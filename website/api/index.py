from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from .v1 import v1
from .v2 import v2

app = FastAPI()
app.include_router(v1)
app.include_router(v2)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api")
async def root():
    return RedirectResponse("/api/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
