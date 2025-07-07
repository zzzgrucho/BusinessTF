import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Importancia de las Características - Random Forest")

# Ejemplo de datos
features = [
    "Género", "DescripciónEstadoCivil", "ID_PuntuaciónDesempeño",
    "SatisfacciónEmpleado", "ConteoProyectosEspeciales",
    "DíasTardeÚltimos30", "Ausencias"
]
importances = [0.05, 0.61, 0.04, 0.12, 0.04, 0.02, 0.11]
df_importance = pd.DataFrame({
    "Feature": features,
    "Importance": importances
}).sort_values("Importance")

# Mostrar dataframe
st.write("### Datos de Importancia", df_importance)

# Crear gráfico
fig, ax = plt.subplots()
ax.barh(df_importance["Feature"], df_importance["Importance"])
ax.set_title("Importancia de las Características - Random Forest")
ax.set_xlabel("Importancia")
st.pyplot(fig)
