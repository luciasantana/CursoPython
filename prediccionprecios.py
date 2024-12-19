#EJERCICIO PREDICCÓN
import gradio as gr

#Definir la función de predicción
def predict_precio(metros_cuadrados, distrito)
    precios_base = {
        "centro" = 3000
        "Norte" = 2500
        "Sur" = 2000
        "Este" = 2200
        "Oeste" = 2400
    }

#Obtener el precio por metro cuadrado del distrito seleccionado 
precio_por_m2 = precios_base.get(distrito, 2000)
precio_total = metros_cuadrados *  precio_por_m2
return f"El preccio estimado es: ${precio_total:,.2f}"

#Lista de distritos disponibles
opciones_distritos = ["centro", "Norte", "Sur", "Este", "Oeste" ]

#Crear la interfax
iface = gr.Interface(
    fn=predict_precio,
    inputs=["number", gr.Dropdown(opciones_distritos)],
    outputs = "text",
    title = "Predicción de precios de inmuebles"
    description = "Introduce los metros cuadrados y seleccione el distrito para predecir el precio"
)