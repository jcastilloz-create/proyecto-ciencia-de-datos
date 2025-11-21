import os,joblib,pandas as pd
BASE_DIR=os.path.dirname(__file__)
MODELS_DIR=os.path.join(BASE_DIR,"models")
FEATURES=["horas_estudio","asistencia","tareas_entregadas","participacion_clase","promedio_previos","uso_plataforma_virtual"]
MODEL_FILES={m:os.path.join(MODELS_DIR,f"{m}_model.pkl") for m in ["knn","mlp","linreg"]}
def load_models():return {n:joblib.load(p) for n,p in MODEL_FILES.items()}
def validate_input(d):
    miss=[f for f in FEATURES if f not in d]
    if miss:raise ValueError(f"Faltan variables: {miss}")
def prepare_input(d):return pd.DataFrame([{f:float(d[f]) for f in FEATURES}])