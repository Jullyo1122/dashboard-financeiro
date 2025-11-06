from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO

app = FastAPI()

dados_importados = None

@app.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...)):
    global dados_importados
    contents = await file.read()
    df = pd.read_excel(BytesIO(contents))
    dados_importados = df
    return {"status": "success", "columns": df.columns.tolist(), "rows": len(df)}

@app.get("/metrics")
def get_metrics():
    global dados_importados
    if dados_importados is None:
        return {"error": "Nenhum arquivo importado."}
    df = dados_importados
    resumo = df.groupby("Mês")["Vendas"].sum().reset_index()
    return {
        "labels": resumo["Mês"].tolist(),
        "values": resumo["Vendas"].tolist()
    }
