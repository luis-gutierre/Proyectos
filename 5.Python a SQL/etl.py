import pandas as pd
from sqlalchemy import create_engine, text
import urllib

# ======
# 1. EXTRAER (desde CSV)
# ======
ventas = pd.read_csv("ventas_grandes.csv")
print("Datos extraídos")
print(ventas)

# ======
# 2. TRANSFORMAR
# ======
# Eliminar nulos
ventas = ventas.dropna()

#Asegurar que fecha sea tipo datetime
ventas["fecha"] = pd.to_datetime(ventas["fecha"], format="%Y-%m-%d")

#Crear nueva columna 'total'
ventas["total"] = ventas["cantidad"] * ventas["precio_unitario"]

print("\nDatos transformados: ")
print(ventas)

# ======
# 3. CARGAR en SQL Server
# ======
# Cadena de conexión con autenticación de Windows
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=DESKTOP-F5U8CON;"
    "DATABASE=ETL_DB;"
    "Trusted_Connection=yes;" #Autenticación de Windows
    "TrustServerCertificate=yes;" #Agregado para evitar error SSL
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

with engine.begin() as conn:
    # 4. Crear tabla temporal
    conn.execute(text("""
        IF OBJECT_ID('tempdb..#TempVentas') IS NOT NULL DROP TABLE #TempVentas;
        CREATE TABLE #TempVentas (
            id_venta INT,
            producto NVARCHAR(100),
            cantidad INT,
            precio_unitario DECIMAL(10,2),
            total DECIMAL(10,2),
            fecha DATE
        );
    """))

    # 5. Insertar datos en tabla temporal
    ventas.to_sql("#TempVentas", con=conn, if_exists="append", index=False)

    # 6. MERGE para hacer UPSERT
    conn.execute(text("""
        MERGE Ventas AS target
        USING #TempVentas AS source
        ON target.id_venta = source.id_venta
        WHEN MATCHED THEN
            UPDATE SET
                target.producto = source.producto,
                target.cantidad = source.cantidad,
                target.precio_unitario = source.precio_unitario,
                target.total = source.total,
                target.fecha = source.fecha
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (id_venta, producto, cantidad, precio_unitario, total, fecha)
            VALUES (source.id_venta, source.producto, source.cantidad, source.precio_unitario, source.total, source.fecha);
    """))

print("\n✅ UPSERT completado: datos insertados/actualizados en SQL Server.")