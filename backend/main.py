from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.pricing_service import calculate_price

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PriceRequest(BaseModel):
    product_id: str
    base_price: float
    zip_code: str


@app.get("/")
def health():
    return {"status": "running"}

@app.post("/pricing")
def pricing(request: PriceRequest):

    return calculate_price(
        request.base_price,
        request.zip_code
    )