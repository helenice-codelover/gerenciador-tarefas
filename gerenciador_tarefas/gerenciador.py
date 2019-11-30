from fastapi import FastAPI

TAREFAS = [
    {"id": 1,"titulo": "Comprar ovos"},
    {"id": 2,"titulo": "Comprar sabonete"},

]

app=FastAPI()

@app.get("/tarefas")
def listar():
    return TAREFAS
