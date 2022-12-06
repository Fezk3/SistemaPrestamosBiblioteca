from Biblioteca import Biblioteca
from datetime import datetime

biblio = Biblioteca()

biblio.all_books()
biblio.all_authors()
biblio.create_directory()

print(f'Bienvenido a la {biblio.name}')

while True:

    print('Menu: ')
    print('1. Solicitar un prestamo de un libro')
    print('2. Mostrar el total de libros prestados de un autor especifico')
    print('3. Mostrar el dia de la semana en el que se realizaron mas prestamos')
    print('4. Mostrar el autor mas solicitado')
    print('5. Mostrar el libro mas solicitado')
    print('6. Salir')
    op = int(input())

    if op == 1:

        fechaact = datetime.now()
        diasemanal = {0: 'lunes', 1: 'martes', 2: 'miercoles', 3: 'jueves', 4: 'viernes', 5: 'sabado', 6: 'domingo'}

        print('Lista de libros de la biblioteca: ')
        print(Biblioteca.books)
        print(f'Lista de autores: ')
        print(Biblioteca.authors)

        libro = input('\nEscriba el nombre del libro que desea: ')
        autor = input('Escriba el nombre del autor del libro: ')
        dia = diasemanal[fechaact.today().weekday()]
        fecha = f'{fechaact.year}-{fechaact.month}-{fechaact.day}'

        if biblio.lend_book(libro, autor, dia, fecha):

            print("Prestamo tramitado con exito\n")

        else:

            print("El prestamo no ha sido tramitado\n")

    elif op == 2:

        print(f'Lista de autores: ')
        print(Biblioteca.authors)

        autor = input('\nEscriba el nombre del autor: ')

        print(f'El total de libros prestados del autor {autor} es: {biblio.author_lended_books(autor)}\n')

    elif op == 3:

        print(f'El dia de la semana con mas prestamos es: {biblio.day_with_highest_lending()}\n')

    elif op == 4:

        print(f'El autor mas solicitado es: {biblio.best_author()}\n')

    elif op == 5:

        print(f'El libro mas solicitado es: {biblio.best_book()}\n')

    elif op == 6:

        print('Gracias por su visita')
        break

    else:

        print('Opcion invalida, intente denuevo\n')