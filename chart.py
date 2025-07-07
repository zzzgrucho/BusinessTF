import streamlit as st
import pandas as pd

st.title("📊 Importancia de las Características - Random Forest")

# Datos de ejemplo
features = [
    "Género", "DescripciónEstadoCivil", "ID_PuntuaciónDesempeño",
    "SatisfacciónEmpleado", "ConteoProyectosEspeciales",
    "DíasTardeÚltimos30", "Ausencias"
]
importances = [0.05, 0.61, 0.04, 0.12, 0.04, 0.02, 0.11]

# Crear DataFrame
df = pd.DataFrame({
    "Característica": features,
    "Importancia": importances
}).sort_values("Importancia", ascending=False)

# Mostrar tabla
st.write("### Tabla de Importancia", df)

# Mostrar gráfico
st.bar_chart(df.set_index("Característica"))

