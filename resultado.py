import csv

# 1. Pedir la ruta del archivo
ruta = input("Ingrese la ruta del archivo CSV: ")

# Lista para guardar resultados
registros_filtrados = []

# 2. Leer el archivo CSV
with open(ruta, mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        sexo = fila["Sexo"]
        edad = int(fila["Edad"])

        # 3. Filtrar mujeres entre 20 y 40 años
        if sexo.lower() == "femenino" and 20 <= edad <= 40:
            registros_filtrados.append(fila)

# 4. Generar nuevo archivo resultado.csv
with open("resultado.csv", mode="w", newline="", encoding="utf-8") as salida:
    campos = ["ID secuencial", "Nombre", "Sexo", "Edad"]
    escritor = csv.DictWriter(salida, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(registros_filtrados)

print("Archivo resultado.csv creado correctamente.")
