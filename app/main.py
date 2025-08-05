
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/legbedje/Documents/nlp-copywriter/static"), name="static")


class Product(BaseModel):
    name: str
    description: str
    target_audience: str


@app.post("/generate-copy")
async def generate_copy(product: Product):
    """
    Generates sales copy based on product information.
    """
    template = f"""
    **Introducing {product.name}!**

    {product.description}

    Perfect for {product.target_audience}.

    Get yours today!
    """
    return {"copy": template}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the NLP Copywriter API!"}
