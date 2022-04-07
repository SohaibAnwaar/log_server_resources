import pandas as pd
import os
from utils import preprocessing, get_graph
from fastapi import FastAPI
import glob
from consts import logs_path
from fastapi.responses import HTMLResponse




app = FastAPI()


@app.get("/GetGraph/{file_name}", response_class=HTMLResponse)
async def GetGraph(file_name: str):
    file_name = f"{logs_path}{file_name}"
    df = pd.read_csv(file_name, sep = "\t")
    df = preprocessing(df)
    return get_graph(df)


@app.get("/get_logs")
async def get_logs():
    files = [i.replace(logs_path, "http://127.0.0.1:8000/GetGraph/") for i in glob.glob(f"{logs_path}*.log")]
    return {"files":files}

@app.get("/")
async def get_dates():
    os.system("nohup bash resource_utilisation.sh &")
    return {"app":"Server logs"}
