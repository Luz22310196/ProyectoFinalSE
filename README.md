# ProyectoFinalSE# 🛒 Sistema Experto de Punto de Venta Inteligente

## 📖 Descripción

El Sistema Experto de Punto de Venta Inteligente es una aplicación desarrollada en Python que permite gestionar ventas e inventario mediante el uso de agentes inteligentes y reglas de inferencia.

El sistema es capaz de interpretar pedidos escritos en lenguaje natural, validar la disponibilidad de productos, actualizar automáticamente el inventario y proporcionar explicaciones sobre las decisiones tomadas durante el proceso.

Este proyecto fue desarrollado como parte de la materia de Sistemas Expertos y tiene como finalidad demostrar la aplicación práctica de la Inteligencia Artificial en la automatización de procesos comerciales.

---

# 🎯 Objetivo

Desarrollar un sistema experto basado en agentes inteligentes capaz de:

- Interpretar solicitudes de clientes.
- Realizar inferencias mediante reglas de negocio.
- Gestionar inventario automáticamente.
- Aplicar validaciones inteligentes.
- Generar recomendaciones automáticas.
- Explicar cada decisión tomada por el sistema.

---

# ⚙️ Tecnologías Utilizadas

- Python
- Streamlit
- SQLite
- GitHub

---

# 🏗️ Arquitectura del Sistema

```text
Cliente
   │
   ▼
Agente Cliente
   │
   ▼
Agente Pedido
   │
   ▼
Base de Datos SQLite
   │
   ▼
Agente Supervisor
   │
   ▼
Usuario
```

## Agente Cliente

Responsable de interpretar el texto ingresado por el usuario y detectar los productos y cantidades solicitadas.

## Agente Pedido

Responsable de:

- Validar la existencia de productos.
- Verificar stock disponible.
- Calcular importes.
- Aplicar descuentos.
- Actualizar inventario.

## Agente Supervisor

Responsable de:

- Analizar el pedido procesado.
- Justificar las decisiones tomadas.
- Emitir recomendaciones.
- Generar explicaciones para el usuario.

---

# 🧠 Reglas de Inferencia

El sistema implementa las siguientes reglas:

1. Validación de disponibilidad de productos.
2. Aplicación de descuentos cuando el monto de compra supera un límite definido.
3. Generación de alertas cuando el stock es insuficiente.
4. Recomendaciones automáticas de reabastecimiento.
5. Detección de compras por volumen.

---

# 🗄️ Base de Datos

El sistema utiliza SQLite como motor de base de datos.

## Tabla Principal: productos

| Campo | Descripción |
|---------|-----------|
| id | Identificador del producto |
| nombre | Nombre del producto |
| precio | Precio unitario |
| stock | Existencia disponible |

La base de datos es utilizada por los agentes inteligentes para realizar inferencias y tomar decisiones durante el procesamiento de pedidos.

---

# 🚀 Instalación

## Clonar el repositorio

```bash
git clone https://github.com/Luz22310196/ProyectoFinalSE.git
```

## Entrar al directorio del proyecto

```bash
cd ProyectoFinalSE
```

## Instalar dependencias

```bash
pip install streamlit
```

---

# ▶️ Ejecución del Sistema

Inicializar la base de datos:

```bash
python DataBase/Init_db.py
```

Insertar datos iniciales:

```bash
python DataBase/Insert_data.py
```

Ejecutar la aplicación:

```bash
streamlit run App/ui.py
```

---

# 💻 Ejemplo de Uso

## Entrada del Usuario

```text
dos arroz y tres leche
```

## Resultado

```text
Pedido generado correctamente

2 x Arroz
3 x Leche

Total calculado

Inventario actualizado
```

El sistema analiza automáticamente la solicitud, valida existencias, calcula importes y genera una explicación del proceso realizado.

---

# 📋 Funcionalidades

## Ventas

- Registro de pedidos.
- Interpretación de lenguaje natural.
- Cálculo automático de totales.
- Aplicación de descuentos.

## Inventario

- Consulta de productos.
- Visualización de existencias.
- Actualización automática después de cada venta.

## Gestión de Productos

- Agregar productos.
- Editar productos.
- Modificar precios.
- Actualizar stock.

## Inteligencia del Sistema

- Validación automática de inventario.
- Detección de stock insuficiente.
- Recomendaciones automáticas.
- Explicabilidad de decisiones.

---

# 📈 Beneficios del Sistema

- Automatización de procesos de venta.
- Reducción de errores humanos.
- Control eficiente de inventario.
- Toma de decisiones basada en reglas.
- Mayor rapidez en la atención al cliente.
- Información actualizada en tiempo real.

---

# 📷 Capturas de Pantalla

Agregar aquí las capturas del sistema:

### Pantalla Principal

![Inicio](images/inicio.png)

### Módulo de Ventas

![Ventas](images/ventas.png)

### Módulo de Inventario

![Inventario](images/inventario.png)

### Gestión de Productos

![Productos](images/productos.png)

---

# 📚 Conclusiones

El Sistema Experto de Punto de Venta Inteligente demuestra la aplicación práctica de los Sistemas Expertos mediante el uso de agentes inteligentes, reglas de inferencia y bases de conocimiento. La solución desarrollada permite automatizar tareas de ventas e inventario, proporcionando soporte inteligente para la toma de decisiones y mejorando la eficiencia operativa de un negocio.

Además, el proyecto evidencia cómo la Inteligencia Artificial puede integrarse en aplicaciones reales para resolver problemas cotidianos de manera eficiente y confiable.

---

# 👩‍💻 Autora

**Luz Aurora Barboza Arteaga**

**Registro:** 22310196

---

# 🔗 Repositorio

Repositorio oficial del proyecto:

https://github.com/Luz22310196/ProyectoFinalSE.git