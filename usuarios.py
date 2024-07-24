from flask import Flask, render_template, Blueprint
usuario_route = Blueprint("usuario", __name__)
"""
    /usuario/ (get)  - index/lista dos remedios cadastrados
    /usuario/ (post)
    /usuario/cadastro  (get) - renderizar o formulario para outro remedio
    /usuarios/<id> (get) obter dados do remedio
    /usuarios/<id>/edit(get) - renderizar o formulario para editar o remedio
    /usuarios/<id>/update(put) - atualizar o remedio
    /usuarios/<id>/delete (delete) - deleta o remedio
"""
#rota para login do gogle
@usuario_route.route("/")
def home():
    return render_template("index.html")
#Ao cadastrar o remedio no /cadastro ele ira para o home e atualizara a pagina e fará a função abaixo inserir_remedio
@usuario_route.route("/", methods=["POST"])
def inserir_remedio():
    pass
@usuario_route.route("/cadastro")
def cadastrar():
    return render_template("gerenciador.html")

@usuario_route.route("/<int:remedio_id>")
def obter_remedio(remedio_id):
    pass
@usuario_route.route("/<int:remedio_id>/edit")
def editar_remedio(remedio_id):
    pass
@usuario_route.route("/<int:remedio_id>/update", methods=["PUT"])
def atualizar_remedio(remedio_id):
    pass
@usuario_route.route("/<id:remedio_id>/delete",methods=["DELETE"])
def deletar_remedio(remedio_id):
    pass