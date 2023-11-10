from UsuarioDao import UsuarioDao
from Usuario import Usuario
from LoggerBase import log

bandera = True

while bandera:
    decision = int(input(f'''
    Opciones:
    1. Lista de usuarios
    2. Agregar usuario
    3. Modificar usuario
    4. Eliminar usuario
    5. Salir

    Escribe tu opción (1-5): '''))

    if decision == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif decision == 2:
        username = input('Ingrese el nombre de usuario: ')
        password = input('Ingrese la contraseña: ')
        nuevoUsuario = Usuario(username=username, password=password)
        usuariosInsertados = UsuarioDao.insertar(nuevoUsuario)
        log.info(f'Se agrego {usuariosInsertados} usuarios')
    
    elif decision == 3:
        idUsuario = input('Ingrese el ID del usuario a modificar: ')
        username = input('Ingrese el nuevo nombre de usuario: ')
        password = input('Ingrese la nueva contraseña: ')
        usuarioModificar = Usuario(idUsuario, username, password)
        usuariosModificados = UsuarioDao.actualizar(usuarioModificar)
        log.info(f'Se modifico {usuariosModificados} usuarios')

    elif decision == 4:
        idUsuario = input('Ingrese el ID del usuario a eliminar: ')
        usuarioEliminar = Usuario(idUsuario)
        usuariosEliminados = UsuarioDao.eliminar(usuarioEliminar)
        log.info(f'Se elimino {usuariosModificados} usuarios')
    
    elif decision == 5:
        bandera = False

    else:
        log.info('Opcion ingresada no valida. Escoger del 1 al 5')

log.info('Saliendo de la aplicación')