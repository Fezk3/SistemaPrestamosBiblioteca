import csv
from statistics import mode


class Biblioteca:

    directory = []
    books = []
    authors = []

    def __init__(self, name='Biblioteca Publica'):
        self.name = name

    def all_books(self):
        with open('libros.csv', 'r') as book:
            libro_reader = csv.reader(book)

            for line in libro_reader:
                Biblioteca.books = line

    def all_authors(self):
        with open('autores.csv', 'r') as author:
            author_reader = csv.reader(author)

            for line in author_reader:
                Biblioteca.authors = line

    def create_directory(self):
        Biblioteca.directory = zip(Biblioteca.books, Biblioteca.authors)

    def lend_book(self, book, author, day, date):
        check = (book, author)

        for reg in Biblioteca.directory:
            if check == reg:
                lend = (book, author, day, date)
                with open('prestamos.csv', 'a', newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(lend)
                    return True

    def author_lended_books(self, author):
        cont = 0

        with open('prestamos.csv', 'r') as lend:
            lend_reader= csv.DictReader(lend)

            for line in lend_reader:
                if author == line['author']:
                    cont += 1

            return cont

    def day_with_highest_lending(self):
        days = []

        with open('prestamos.csv', 'r') as prestamous:
            presta_reader = csv.DictReader(prestamous)

            next(presta_reader)

            for line in presta_reader:
                x = line['dia']
                days.append(x)

        mas = mode(days)

        return mas

    def best_author(self):
        author_mas = []

        with open('prestamos.csv', 'r') as prestamous:
            author_read = csv.DictReader(prestamous)

            next(author_read)

            for line in author_read:
                x = line['autor']
                author_mas.append(x)

        mas = mode(author_mas)

        return mas

    def best_book(self):
        book_mas = []

        with open('prestamos.csv', 'r') as libs:
            lib_reader = csv.DictReader(libs)

            next(lib_reader)

            for line in lib_reader:
                x = line['libro']
                book_mas.append(x)

        mas = mode(book_mas)

        return mas

    def info_books(self):
        with open('Libros.csv', 'r') as libro:
            libro_reader = csv.reader(libro)  # list of everything on the Libros file

            for line in libro_reader:
                libros = line
            print(libros)

    def info_authors(self):
        with open('autores.csv', 'r') as author:
            author_reader = csv.reader(author)  # list of autores file

            for line in author_reader:
                authors = line
            print(authors)
