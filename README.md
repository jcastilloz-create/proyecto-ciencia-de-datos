Juanita Castillo
Cédula: 1002544997
Este proyecto tiene como objetivo aplicar paso a paso la metodología completa del ciclo de ciencia de datos usando un conjunto de datos académico.

El propósito es desarrollar, entrenar y desplegar un modelo de machine learning capaz de predecir el puntaje final de un estudiante a partir de variables relacionadas con sus hábitos académicos, desempeño y participación.

El proyecto incluye:

Limpieza y preparación de datos
Ingeniería de atributos
Entrenamiento de 3 modelos (KNN, MLP y Regresión Lineal)
Evaluación de desempeño
Comparación de los modelos
API con Flask para realizar predicciones
Interfaz web donde el usuario ingresa variables y recibe la predicción
Documentación completa y estructura profesional
Repositorio en GitHub con frontend + backend

2. Variable Objetivo y Variables Predictoras
3. Variable objetivo

puntaje_final
Es una variable numérica que representa el rendimiento final del estudiante.

Variables predictoras (features)
Variable	Descripción
horas_estudio	Horas promedio de estudio semanal
asistencia	Porcentaje de asistencia a clase
tareas_entregadas	Cantidad de tareas entregadas
participacion_clase	Nivel de participación (0-10)
promedio_previos	Promedio académico anterior (0-5)
uso_plataforma_virtual	Cantidad de horas usando Moodle/Teams/Blackboard
3. Metodología Aplicada

Carga y exploración inicial del dataset

Limpieza de datos

Análisis exploratorio (EDA)

Normalización / escalado

Separación en train/test

Entrenamiento de modelos:

KNN

MLPRegressor

Regresión lineal

Evaluación (MSE y R²)

Guardado de modelos con joblib

Despliegue del backend (API con Flask)

Construcción del frontend

Integración total (frontend + backend)
4. Evaluación de Modelos

El script train.py entrena los tres modelos y muestra los resultados en consola:

MSE (Error Cuadrático Medio)

R² (Coeficiente de determinación)

Los modelos entrenados se guardan en:

backend/models/

5. Estructura del Proyecto
proyecto_ciencia_datos/
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── utils.py
│   ├── train.py
│   ├── requirements.txt
│   └── models/
│       ├── knn_model.pkl
│       ├── mlp_model.pkl
│       └── linreg_model.pkl
│
├── data/
│   └── estudiantes.csv
│
└── README.md

6. Cómo ejecutar el proyecto
7.  Backend (API con Flask)
1. Abrir una terminal dentro de la carpeta backend/.
2. Instalar dependencias:
pip install -r requirements.txt

3. Ejecutar la API:
python app.py


La API quedará activa en:
http://127.0.0.1:5000

Frontend (Interfaz Web)

Abrir la carpeta frontend/

Dar doble clic en:

index.html


La página abrirá en tu navegador y podrás hacer predicciones.


Esto generará los modelos actualizados en:
backend/models/

7. Uso del Sistema

El usuario abre la interfaz web.

Ingresa valores en los campos:

horas de estudio

asistencia

tareas entregadas

participación

promedio previo

uso plataforma

Selecciona el modelo o “todos”.

El sistema envía la solicitud al backend.

Flask devuelve la predicción.

El frontend muestra el resultado.
