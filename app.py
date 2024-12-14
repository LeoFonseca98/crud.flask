import uuid
from flask import Flask, jsonify, redirect, render_template,request, url_for
from esquema.esquema import Usuario

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

'''
        CRUD DE USUÁRIOS

    1. Adicionar usuarios e criar o banco de dados no postgres.
        Usuario - Nome, email, profissão
    2. Listar usuários.
    3. Editar usuários.
    4. Excluir usuários.

'''

@app.route('/adicionar_usuario')
def adicionar_usuario():
  return render_template('adicionar_usuario.html')


@app.route('/inserir_usuario', methods=['POST'])
def inserir_usuario():
  try:
      user_id = str(uuid.uuid4())

      id = user_id
      nome = request.form['nome']
      email = request.form['email']
      profissao = request.form['profissao']

      novo_usuario = Usuario.create(id=id, nome=nome, email=email, profissao=profissao)
      novo_usuario.save()

      return redirect(url_for('index'))
      #return jsonify({"message": "Usuário inserido com sucesso!", "id": novo_usuario.id}), 201

  except Exception as e:
    print(f'Erro inesperado: {e}')
    return jsonify({"message": "Erro ao inserir usuário", "error": str(e)}), 500


@app.route('/listar_usuarios')
def listar_usuarios():

    usuarios = Usuario.select()


    usuarios_lista = [
      {  
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "profissao": usuario.profissao
      }
      for usuario in usuarios
    ]
    
    return render_template('listar_usuarios.html', usuarios=usuarios_lista)

@app.route('/editar_usuario/<string:id>', methods=['GET'])
def editar_usuario(id):
  usuario = Usuario.get_or_none(Usuario.id == id)

  if not usuario:
    return jsonify({"message": "Usuário não encontrado"}), 404
  
  return render_template('editar_usuario.html', usuario=usuario)

@app.route('/form_editar/<string:id>', methods=['POST'])
def form_editar(id):

  try:
      usuario = Usuario.get_or_none(Usuario.id == id)

      if not usuario:
        return jsonify({"message": "Usuário não encontrado!" })

      usuario.email = request.form.get('email')
      usuario.profissao = request.form.get('profissao')
      usuario.save()
      #return jsonify({"message": "Usuário editado com sucesso!"})
      return redirect(url_for('index'))
  
  except Exception as e:
    print(f'Erro inesperado! {e}')
    return jsonify({"message":"Erro ao inserir usuário", "error": str(e)})
  

@app.route('/deletar_usuario/<string:id>', methods=['GET', 'POST'])
def deletar_usuario(id):

  try:
    usuario = Usuario.get_or_none(Usuario.id == id)

    if not usuario:
      return jsonify({"message":"Usuário não encontrado!"})
      
    usuario.delete_instance()
    return redirect(url_for('index'))

  except Exception as e:
    print(f'Erro inesperado! {e}')
    return jsonify({"message":"Erro ao inserir usuário", "error": str(e)})

if __name__=='__main__':
  app.run(debug=True)