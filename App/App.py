import streamlit as st

st.set_page_config(
    page_title="Sistema Experto de Ventas",
    layout="centered"
)

st.title("Sistema Experto de Ventas")
st.write("Ingrese su solicitud para analizarla y generar una respuesta estructurada.")

# Entrada
mensaje = st.text_area(
    "Solicitud del usuario:",
    placeholder="Ejemplo: Necesito 3 motores NEMA17 y 2 drivers",
    height=120
)

# Botón
if st.button("Procesar solicitud"):

    if mensaje.strip() == "":
        st.warning("Debe ingresar una solicitud antes de procesar.")
    else:
        st.success("Solicitud recibida correctamente")

        st.subheader("Entrada procesada")
        st.write(mensaje)

        # Simulación de sistema experto (puedes reemplazar esto luego)
        st.subheader("Resultado del sistema experto")

        # Ejemplo simple de reglas simuladas
        if "motor" in mensaje.lower():
            st.write("Se detectaron componentes de tipo motor.")
        if "driver" in mensaje.lower():
            st.write("Se detectaron drivers en la solicitud.")

        st.info("El sistema aún se encuentra en fase de reglas básicas.")