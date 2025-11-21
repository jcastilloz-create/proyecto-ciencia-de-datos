from flask import Flask,request,jsonify
from utils import load_models,validate_input,prepare_input
app=Flask(__name__)
MODELS=load_models()
@app.route("/predict",methods=["POST"])
def predict():
    try:
        d=request.get_json()
        validate_input(d)
        X=prepare_input(d)
        m=d.get("modelo")
        if m in MODELS:
            return jsonify({"modelo":m,"prediccion":float(MODELS[m].predict(X)[0])})
        if m=="todos":
            return jsonify({name:float(model.predict(X)[0]) for name,model in MODELS.items()})
        return jsonify({"error":"Modelo inválido"})
    except Exception as e:
        return jsonify({"error":str(e)})
@app.route("/")
def home():return "API funcionando correctamente"
if __name__=="__main__":app.run(port=5000,debug=True)