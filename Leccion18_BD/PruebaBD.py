import psycopg2

# Metodo para conectarse a la base de datos
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5433',
    database='test_db')

print(conexion)

# Cursor: Sirve para ejecutar sentencias en SQL

cursor = conexion.cursor()

# Sentencia a enviar por SQL
sentencia = 'SELECT * FROM "personasAdmitidas"'

# Ejecución de la sentencia
cursor.execute(sentencia)

# Obtener el resultado de ejecutar la sentencia

registros = cursor.fetchall()

print(registros)

# Cerrar el registro

cursor.close()
conexion.close()


