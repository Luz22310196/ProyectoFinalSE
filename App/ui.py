import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import sqlite3
from Agents.Cliente import interpretar_mensaje
from Agents.Pedido import generar_pedido
from Agents.Supervisor import explicar

st.set_page_config(page_title="POS Inteligente", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #e0f2fe;
    color: #1e3a8a;
}
h1 { color:#1d4ed8; }

section[data-testid="stSidebar"] {
    background-color: #1e40af;
}

.stButton button {
    width:100%;
    height:45px;
    background:#3b82f6;
    color:white;
}

.caja {
    background:white;
    padding:15px;
    border-radius:10px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

st.title("Punto de Venta Inteligente")

def obtener_productos():
    conn = sqlite3.connect("DataBase/Sistema.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, stock FROM productos")
    data = cursor.fetchall()
    conn.close()
    return data

def agregar_producto(nombre, precio, stock):
    conn = sqlite3.connect("DataBase/Sistema.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos VALUES (NULL, ?, ?, ?)", (nombre, precio, stock))
    conn.commit()
    conn.close()

st.sidebar.title("Menu")

if "menu" not in st.session_state:
    st.session_state.menu = "ventas"

if st.sidebar.button("Ventas"):
    st.session_state.menu = "ventas"

if st.sidebar.button("Inventario"):
    st.session_state.menu = "inventario"

if st.sidebar.button("Agregar producto"):
    st.session_state.menu = "agregar"

if st.sidebar.button("Editar producto"):
    st.session_state.menu = "editar"

# VENTAS
if st.session_state.menu == "ventas":

    msg = st.text_input("Ejemplo: dos arroz")

    if st.button("Procesar pedido"):

        productos = interpretar_mensaje(msg)

        if productos:
            detalle, total, alertas = generar_pedido(productos)
            resultado = explicar(detalle, total, alertas)
            st.markdown(f"<div class='caja'>{resultado}</div>", unsafe_allow_html=True)
        else:
            st.warning("Pedido no entendido")

# INVENTARIO
elif st.session_state.menu == "inventario":

    productos = obtener_productos()

    for p in productos:
        st.markdown(f"<div class='caja'><b>{p[0]}</b><br>Precio: {p[1]}<br>Stock: {p[2]}</div>", unsafe_allow_html=True)

# AGREGAR
elif st.session_state.menu == "agregar":

    nombre = st.text_input("Nombre")
    precio = st.number_input("Precio", min_value=1)
    stock = st.number_input("Stock", min_value=0)

    if st.button("Guardar"):
        agregar_producto(nombre.lower(), precio, stock)
        st.success("Producto agregado")

# EDITAR
elif st.session_state.menu == "editar":

    productos = obtener_productos()
    nombres = [p[0] for p in productos]

    if nombres:

        seleccionado = st.selectbox("Producto", nombres)
        datos = [p for p in productos if p[0] == seleccionado][0]

        nuevo_nombre = st.text_input("Nombre", value=datos[0])
        nuevo_precio = st.number_input("Precio", value=datos[1])
        nuevo_stock = st.number_input("Stock", value=datos[2])

        if st.button("Actualizar"):

            conn = sqlite3.connect("DataBase/Sistema.db")
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE productos SET nombre=?, precio=?, stock=? WHERE nombre=?",
                (nuevo_nombre.lower(), nuevo_precio, nuevo_stock, seleccionado)
            )

            conn.commit()
            conn.close()

            st.success("Producto actualizado correctamente")

    else:
        st.warning("No hay productos")