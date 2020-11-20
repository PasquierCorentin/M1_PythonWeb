from Flask import Flask
from flask import render_template, request, jsonify, json

from datetime import datetime


app = Flask(__name__)



#On instancie notre livre

def loadJson(path):
    f = open(path)
    loadedJson = json.load(f)
    f.close()
    return loadedJson


booklist = loadJson("app/data/books.json")


#On défini les routes
@app.route("/")

def index():
	return render_template("public/index.html")


@app.route("/api/books", methods=['GET'])

def afficher_book() :
	return jsonify(booklist)

@app.route('/api/books/<int:book_id>', methods=['GET'])

def book_id_search(book_id):

    livres_trouve = []

    for book in booklist:

        if book['id'] == book_id:

            livres_trouve.append(book)
            return jsonify(livres_trouve)

        else :
            return 'Aucun livre ne porte cet id'

@app.route('/api/books/<string:book_title>')

def book_title_search(book_title) :

	find_book = []

	for book in booklist :

		if book['titre'] == book_title :

			find_book.append(book)
			return jsonify(find_book)

		else :

			return "Aucun livre ne porte ce titre"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
