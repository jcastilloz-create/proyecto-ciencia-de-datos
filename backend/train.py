import os,sys,pandas as pd,joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
BASE=os.path.dirname(__file__)
DATA=os.path.join(BASE,"..","data","estudiantes.csv")
OUT=os.path.join(BASE,"models")
os.makedirs(OUT,exist_ok=True)
FEATURES=["horas_estudio","asistencia","tareas_entregadas","participacion_clase","promedio_previos","uso_plataforma_virtual"]
df=pd.read_csv(DATA)
X=df[FEATURES]
y=df["puntaje_final"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
models={"knn":KNeighborsRegressor(5),
        "mlp":MLPRegressor(hidden_layer_sizes=(64,32),max_iter=500,random_state=42),
        "linreg":LinearRegression()}
for name,mdl in models.items():
    pipe=Pipeline([("scaler",StandardScaler()),(name,mdl)])
    pipe.fit(Xtr,ytr)
    pred=pipe.predict(Xte)
    print(name,"MSE:",mean_squared_error(yte,pred),"R2:",r2_score(yte,pred))
    joblib.dump(pipe,os.path.join(OUT,f"{name}_model.pkl"))