from fastapi import FastAPI
from app.schemas import FormatRequest
from app.formatter import wrap_text, justify_text

app = FastAPI()

@app.post("/quebrar-texto")
def wrap_text_endpoint(req: FormatRequest):
    lines = wrap_text(req.text, req.limit)
    return {"lines": lines}

@app.post("/justificar-texto")
def justify_text_endpoint(req: FormatRequest):
    lines = justify_text(req.text, req.limit)
    return {"lines": lines}
