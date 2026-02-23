from fastapi import FastAPI, HTTPException
from crud import carregar_dados, adicionar_gasto, excluir_gasto, gastos_totais, gastos_por_categoria, gastos_por_ano
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
carregar_dados()

@app.post("/gastos/")
def create_gasto(mes: str, item: str, valor: float, categoria: str):
    if not adicionar_gasto(mes, item, valor, categoria):
        raise HTTPException(status_code=400, detail="Formato inválido. Use MM/YYYY")
    return {"msg": f"Gasto '{item}' adicionado em {mes}"}

@app.delete("/gastos/")
def delete_gasto(mes: str, item: str):
    if excluir_gasto(mes, item):
        return {"msg": f"Gasto '{item}' removido de {mes}"}
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.get("/gastos/")
def total_gastos(mes: str):
    total = gastos_totais(mes)
    if total is None:
        raise HTTPException(status_code=404, detail="Mês não encontrado")
    return {"mes": mes, "total": total}

@app.get("/gastos/{mes}/categorias")
def relatorio_categorias(mes: str):
    categorias = gastos_por_categoria(mes)
    if categorias is None:
        raise HTTPException(status_code=404, detail="Mês não encontrado")
    return {"mes": mes, "gastos_por_categoria": categorias}

@app.get("/gastos/ano/{ano}")
def relatorio_anual(ano: str):
    totais = gastos_por_ano(ano)
    if not totais:
        raise HTTPException(status_code=404, detail="Nenhum gasto encontrado para esse ano")
    return {"ano": ano, "totais_por_mes": totais, "total_anual": sum(totais.values())}



app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join("static", "index.html"))
