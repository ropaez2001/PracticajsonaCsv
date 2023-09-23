import json

Datos={} # creo la variable datos de tipo diccionario
Datos["Clientes"]=[]  # dento de datos que es un diccionario creo una lista
Datos["Clientes"].append({
    
            "nombreColor":"rojo",
            "valorHexadec":"#f00"
        }),
Datos["Clientes"].append({
            "nombreColor":"verde",
            "valorHexadec":"#0f0"
        }),
Datos["Clientes"].append({
            "nombreColor":"azul",
            "valorHexadec":"#00f"
        }),
Datos["Clientes"].append({
            "nombreColor":"cyan",
            "valorHexadec":"#0ff"
        }),
Datos["Clientes"].append({
            "nombreColor":"magenta",
            "valorHexadec":"#f0f"
        }),
Datos["Clientes"].append({
            "nombreColor":"amarillo",
            "valorHexadec":"#ff0"
        }),
Datos["Clientes"].append({
            "nombreColor":"negro",
            "valorHexadec":"#000"
        })
    

with open("Datos.json", "w") as file:
    json.dump(Datos,file, indent=4)
    
import json
import csv

# Leer el archivo JSON
with open("Datos.json", "r") as json_file:
    data = json.load(json_file)

# Obtener la lista de clientes del diccionario
clientes = data.get("Clientes", [])

# Crear un archivo CSV y escribir los datos en él con espacio como delimitador
with open("Clientes.csv", "w", newline="") as csv_file:
    # Usar un tabulador como delimitador personalizado
    csv = csv.writer(csv_file)

    # Escribir los encabezados
    csv.writerow(["nombreColor", "valorHexadec"])

    # Usar un bucle for  para iterar sobre la lista de clientes sobre cada fila
    for fila in range(len(clientes)):
        cliente = clientes[fila]
        csv.writerow([cliente["nombreColor"], cliente["valorHexadec"]])