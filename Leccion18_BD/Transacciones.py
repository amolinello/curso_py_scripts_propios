# Manejo de transacciones, es decir, ejecuta todos los query's que modifique la bd de manera correcta
# de lo contrario hace un rollback (si de todas las transacciones 1 falla, se hace rollback a todas)

import psycopg2 as bd

# Postgres no muestra el detalle del error, y esto se puede corregir (ejm: usuario incorrecto)
conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5433',database='test_db')

try:
    conexion.autocommit = False # No se guarda los cambios al ejecutar la sentencia
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO "personasAdmitidas"(nombre, apellido, mail) VALUES(%s, %s, %s)'
    valores = ('Chon', 'Lee123456789123456789', 'lechon@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()
    print('Termina la transaccion')
    
except Exception as ex:
    conexion.rollback()
    print('se hizo rollback')
    print(f'Ocurrio un ERROR\n {ex}')

finally:
    
    conexion.close()

# Es mejor practica usar todo con with
