import pandas as pd
import os
from fpdf import FPDF

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_dataframe():
    limpiar_pantalla()
    print("=== LECTOR Y FILTRADO DE DATOS ===")
    ruta = input("\nIntroduce el nombre o ruta del archivo (ej: datos.csv): ").strip()
    
    if not os.path.exists(ruta):
        print(f"\n[Error]: No se encuentra el archivo en: {os.path.abspath(ruta)}")
        return None
    
    try:
        df = pd.read_csv(ruta)
        print(f"\n✅ Archivo cargado con éxito.")
        print(f"Columnas detectadas: {list(df.columns)}")
        return df
    except Exception as e:
        print(f"❌ Error al procesar el CSV: {e}")
        return None

def filtrar_datos(df):
    print("\n--- Configuración de Filtro ---")
    columna = input("¿Por qué columna deseas filtrar?: ")
    
    if columna not in df.columns:
        print("La columna no existe en el archivo.")
        return df

    valor = input(f"Introduce el valor para buscar en '{columna}': ")

    try:
        tipo = df[columna].dtype
        if tipo == 'int64': valor = int(valor)
        elif tipo == 'float64': valor = float(valor)
    except:
        pass 

    resultado = df[df[columna] == valor]
    print(f"\nSe encontraron {len(resultado)} coincidencias.")
    return resultado

def exportar_a_pdf(df, nombre_archivo):
    """Función auxiliar para convertir el DataFrame en una tabla PDF"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    
    # Título
    pdf.cell(190, 10, "Reporte de Datos Filtrados", ln=True, align='C')
    pdf.ln(10)
    
    # Configuración de tabla
    pdf.set_font("Arial", 'B', 10)
    col_width = 190 / len(df.columns)  # Dividir el ancho de página entre columnas
    
    # Cabeceras
    for col in df.columns:
        pdf.cell(col_width, 10, str(col), border=1, align='C')
    pdf.ln()
    
    # Datos
    pdf.set_font("Arial", '', 9)
    for _, row in df.iterrows():
        for item in row:
            pdf.cell(col_width, 10, str(item), border=1)
        pdf.ln()
    
    nombre_final = f"{nombre_archivo}.pdf"
    pdf.output(nombre_final)
    print(f"✅ Reporte PDF generado como: {nombre_final}")

def exportar_datos(df):
    if df.empty:
        print("No hay datos para exportar.")
        return

    print("\n--- Opciones de Salida ---")
    print("1. Guardar como CSV")
    print("2. Guardar como PDF")
    opcion = input("Selecciona una opción (1 o 2): ")
    
    nombre_archivo = input("Nombre del nuevo archivo (sin extensión): ").strip()

    if opcion == "1":
        nombre_final = f"{nombre_archivo}.csv"
        df.to_csv(nombre_final, index=False)
        print(f"✅ Archivo guardado como: {nombre_final}")
    
    elif opcion == "2":
        exportar_a_pdf(df, nombre_archivo)
    
    else:
        print("Opción no válida.")

def main():
    df = obtener_dataframe()
    if df is not None:
        df_filtrado = filtrar_datos(df)
        exportar_datos(df_filtrado)
        print("\nProceso finalizado.")

if __name__ == "__main__":
    main()