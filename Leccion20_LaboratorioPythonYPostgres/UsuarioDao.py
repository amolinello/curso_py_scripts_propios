
from Usuario import Usuario
from CursorDelPool import CursorDelPool
from LoggerBase import log

class UsuarioDao:

    _SELECCIONAR = 'SELECT * FROM "usuarios"'
    _INSERTAR = 'INSERT INTO "usuarios"(username, "password") VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE "usuarios" SET username = %s, "password" = %s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM "usuarios" WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            listausuarios = []

            for registro in registros:
                registrousuario = Usuario(*registro)
                listausuarios.append(registrousuario)
            
            return listausuarios

    @classmethod
    def insertar(cls, usuario):
        
        with CursorDelPool() as cursor:

            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario a insertar: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        
        with CursorDelPool() as cursor:

            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario a actualizar: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        
        with CursorDelPool() as cursor:

            valores = (usuario.id_usuario, )
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario a borrar: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':

    #DataEliminar = Usuario(5)
    #usuariosEliminados = UsuarioDao.eliminar(DataEliminar)
    #log.debug(f'Usuarios Eliminados: {usuariosEliminados}')

    # usuariosActualizado = Usuario(5, 'Nonameraro', '+123+Random')
    # actualizarDatos = UsuarioDao.actualizar(usuariosActualizado)
    # log.debug(f'Usuarios Actualizados: {actualizarDatos}')

    # usuarioUno = Usuario(username='AM101723', password='Random123+')
    # insetarDatos = UsuarioDao.insertar(usuarioUno)
    # log.debug(f'Usuarios insertados: {insetarDatos}')

    usuariosEnBD = UsuarioDao.seleccionar()
    for dato in usuariosEnBD:
        log.debug(f'Usuarios en BD: {dato}')