import redis

HOST = "localhost"
PORT = 6379


def seed():
    words = [
        {'word': 'Xopa', 'description': 'Forma coloquial de decir Hola.'},
        {'word': 'Chantin', 'description': 'Casa'}
    ]

    for definition in words:
        result_set = redis_con.get(definition['word'])
        if result_set is not None:
            continue

        redis_con.set(definition['word'], definition['description'])


def show(word):
    result_set = redis_con.get(word)

    if result_set is None:
        print(f"No se encontró la palabra: {word}")

    print(result_set)


def show_all():
    for r_key in redis_con.keys():
        print(f"{r_key}: {redis_con.get(r_key)}")


def update(word, description):
    result_set = redis_con.get(word)

    if result_set is None:
        print(f"No se encontró la palabra: {word}")

    redis_con.set(word, description)


def add():
    word = input('Palabra: ')
    description = input('Definicion: ')

    result_set = redis_con.get(word)

    if result_set is not None:
        print(f"La palabra, {word}, ya existe")
        return

    redis_con.set(word, description)


def delete(word):
    result_set = redis_con.get(word)

    if result_set is None:
        print(f"No se encontró la palabra: {word}")

    result_set = redis_con.delete(word)


if __name__ == '__main__':
    redis_con = redis.Redis(host=HOST, port=PORT, db=0, charset="utf-8", decode_responses=True)
    seed()

    while True:
        print('Menu')
        print('1- Mostrar todo')
        print('2- Agregar')
        print('3- Buscar palabra')
        print('4- Actualizar palabra')
        print('5- Borrar palabra')
        print('6- Salir')
        option = int(input('Opcion (1-6): '))

        if option == 1:
            show_all()
        elif option == 2:
            add()
        elif option == 3:
            search_word = input('Palabra: ')
            show(search_word)
        elif option == 4:
            search_word = input('Palabra: ')
            update_description = input('Definicion: ')
            update(search_word, update_description)
        elif option == 5:
            search_word = input('Palabra: ')
            delete(search_word)
        else:
            break
            
