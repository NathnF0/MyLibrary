from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mylibrary.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(30), nullable=False)


@app.route("/")
def home():
    livros = Livro.query.all()

    total_livros = len(livros)
    livros_lendo = len([livro for livro in livros if livro.status == "lendo"])
    livros_concluidos = len([livro for livro in livros if livro.status == "concluido"])

    return render_template(
        "index.html",
        livros=livros,
        total_livros=total_livros,
        livros_lendo=livros_lendo,
        livros_concluidos=livros_concluidos
    )

@app.route("/perfil")
def profile():
    livros = Livro.query.all()

    total_livros = len(livros)
    livros_lendo = len([livro for livro in livros if livro.status == "lendo"])
    livros_concluidos = len([livro for livro in livros if livro.status == "concluido"])

    leitor_ativo = livros_concluidos >= 1

    nivel = min(total_livros // 3 + 1, 10)

    if nivel < 10:
        livros_proximo_nivel = nivel * 3
        progresso = (total_livros % 3) / 3 * 100
    else:
        livros_proximo_nivel = total_livros
        progresso = 100

    primeira_leitura = total_livros >= 1
    leitor_iniciante = total_livros >= 3

    return render_template(
    "profile.html",
    total_livros=total_livros,
    livros_lendo=livros_lendo,
    livros_concluidos=livros_concluidos,
    nivel=nivel,
    livros_proximo_nivel=livros_proximo_nivel,
    progresso=progresso,
    primeira_leitura=primeira_leitura,
    leitor_iniciante=leitor_iniciante,
    leitor_ativo=leitor_ativo
)

@app.route("/adicionar", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        status = request.form["status"]

        livro = Livro(
            title=title,
            author=author,
            status=status
        )

        db.session.add(livro)
        db.session.commit()

        return redirect("/")

    return render_template("add_book.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    livro = Livro.query.get_or_404(id)

    if request.method == "POST":
        livro.title = request.form["title"]
        livro.author = request.form["author"]
        livro.status = request.form["status"]

        db.session.commit()

        return redirect("/")

    return render_template("edit_book.html", livro=livro)

@app.route("/excluir/<int:id>", methods=["POST"])
def delete_book(id):
    livro = Livro.query.get_or_404(id)

    db.session.delete(livro)
    db.session.commit()

    return redirect("/")

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)