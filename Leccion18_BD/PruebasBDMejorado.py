import psycopg2

# Postgres no muestra el detalle del error, y esto se puede corregir (ejm: usuario incorrecto)
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5433',
    database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            ###########################################################################################
            print('UNO'.center(50, '*'))
            sentencia = 'SELECT * FROM "personasAdmitidas"'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)

            ###########################################################################################
            print('DOS'.center(50, '*'))
            sentencia2 = 'SELECT id_persona, nombre FROM "personasAdmitidas"'
            cursor.execute(sentencia2)
            registros2 = cursor.fetchall()
            print(registros2)

            ###########################################################################################
            print('TRES'.center(50, '*'))
            sentencia3 = 'SELECT id_persona, nombre FROM "personasAdmitidas" WHERE id_persona = 4'
            cursor.execute(sentencia3)
            registros3 = cursor.fetchall()
            print(registros3)

            ###########################################################################################
            print('CUATRO'.center(50, '*'))
            # Traer todos los registros
            sentencia4 = 'SELECT id_persona, nombre FROM "personasAdmitidas" WHERE id_persona = %s'
            id_persona = input('Ingrese el ID persona a buscar: ')
            cursor.execute(sentencia4, (id_persona, ))
            registros4 = cursor.fetchall()
            print(registros4)
            
            ###########################################################################################
            print('CINCO'.center(50, '*'))
            # Traer solo un registro
            sentencia5 = 'SELECT id_persona, nombre FROM "personasAdmitidas" WHERE id_persona = %s'
            id_persona = input('Ingrese el ID persona a buscar: ')
            cursor.execute(sentencia5, (id_persona, ))
            registros5 = cursor.fetchone()
            print(registros5)

            ###########################################################################################
            print('SEIS'.center(50, '*'))
            sentencia6 = 'SELECT id_persona, nombre FROM "personasAdmitidas" WHERE id_persona IN (1, 3)'
            # id_persona = input('Ingrese el ID persona a buscar: ')
            cursor.execute(sentencia6)
            registros6 = cursor.fetchall()
            print(registros6)
            for registro in registros6:
                print(registro)

            ###########################################################################################
            print('SIETE'.center(50, '*'))
            sentencia7 = 'SELECT id_persona, nombre FROM "personasAdmitidas" WHERE id_persona IN %s'
            # llaves_primarias = ((1, 2, 3), )
            entrada = input('Ingrese los ID\'s a buscar (Separados por coma): ')
            llaves_primarias = (tuple(entrada.split(',')), )
            cursor.execute(sentencia7, llaves_primarias)
            registros7 = cursor.fetchall()
            print(registros7)
            for registro in registros7:
                print(registro)

            ###########################################################################################
            '''
            sentenciaInsertar = 'INSERT INTO "personasAdmitidas"(nombre, apellido, mail) VALUES(%s,%s,%s)'
            datos = ('Angel', 'Domingo', 'adomingo@mail.com')
            cursor.execute(sentenciaInsertar, datos)
            # conexion.commit() # Guarda los cambios en la base de datos, con el with ya se hace el commit automaticamente
            

            sentencia = 'SELECT * FROM "personasAdmitidas"'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

            ###########################################################################################

            # INSERTAR MUCHOS REGISTROS
            
            sentenciaInsertar = 'INSERT INTO "personasAdmitidas"(nombre, apellido, mail) VALUES(%s,%s,%s)'
            datos = (
                ('Maria', 'Perez', 'mperez@mail.com'),
                ('Catalina', 'Duque', 'cduque@mail.com'),
                ('Lorena', 'Gomez', 'lgomez@mail.com'))
            cursor.executemany(sentenciaInsertar, datos)
            '''
            # # Si uno de estos registros falla en ingresar, se hace rollback, es decir, no inserta los registros que llevaba hasta el momento
            # Deja todo como Estaba antes
            
            sentencia = 'SELECT * FROM "personasAdmitidas"'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

            ###########################################################################################
            print('OCHO'.center(50, '*'))
            sentencia = 'UPDATE "personasAdmitidas" SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s'
            valores = ('Camila', 'Ospina', 'cospina@mail.com', 3)
            cursor.execute(sentencia, valores)

            '''
            valores = (
                ('Camila', 'Ospina', 'cospina@mail.com', 3),
                ('Sebastian', 'Ospina', 'sospina@mail.com', 1),
                ('Camila', 'Ospina', 'cospina@mail.com', 5))
            cursor.executemany(sentencia, valores)
            '''

            sentencia = 'SELECT * FROM "personasAdmitidas"'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

            ###########################################################################################
            print('NUEVE'.center(50, '*'))
            sentencia = 'DELETE FROM "personasAdmitidas" WHERE id_persona IN %s'
            # Se hace lo mismo que en SIETE para eliminar varios registros a la vez
            # Si se va a eliminar solo uno, se puede usar el = en vez de IN
            
            

except Exception as ex:
    print(f'Ocurrio un ERROR\n {ex}')

finally:
    conexion.close()