import requests

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    pokemon = {"name":"weedle"}
    respuesta = requests.get(url)
    print(respuesta)

    if respuesta.status_code == 200:
        # Guarda la lista de los pokemon en una txt
        '''
        contenido = respuesta.content
        with open('Log Prueba API2','wb') as file:
            file.write(contenido)
        '''
        # Imprime los nombres de los pokemon
        '''
        contenido_respuesta = respuesta.json()
        resultado = contenido_respuesta.get('results', [])
        if resultado:
            for pokemon in resultado:
                name = pokemon['name']
                print(name)'''
        
    # La API no recibe POST, solo permite GET
        