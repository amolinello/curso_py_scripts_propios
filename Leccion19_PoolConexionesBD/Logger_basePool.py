import logging as log

#log.basicConfig(level=log.DEBUG)

# Mandar y manejar información en un archivo

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capadatos.log'),
                    log.StreamHandler()
                ]) 
# Cuando se mando el error, su nivel y el nombre del archivo



if __name__ == '__main__':

    # log.basicConfig(level=log.INFO) # Dependiendo del tipo de configuracion muestra el tipo de log
                                    # El tipo DEBUG muestra todo, el tipo INFO no muestra el DEBUG pero si el resto, etc

    log.debug('Mensaje a nivel debug')

    #log.basicConfig(level=log.CRITICAL)

    log.critical('Mensaje a nivel critico')

    #log.basicConfig(level=log.ERROR)

    log.error('Mensaje a nivel error')

    #log.basicConfig(level=log.INFO)

    log.info('Mensaje a nivel info')

    #log.basicConfig(level=log.INFO)

    log.warning('Mensaje a nivel warning')

