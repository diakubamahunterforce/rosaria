from  flask  import  Flask , request,jsonify
from  models .models import db_consulta

app=Flask(__name__)






@app.route("/login",methods=['POST'])

def  LOgin():
    senha_gmail=request.get_json()
    senha=senha_gmail['senha']
    email=senha_gmail['email']
    resposta=db_consulta.iniciar_login(senha=senha,email=email)
    return resposta


@app.route("/consultar",methods=['POST'])
def l1ivro():
    resposta=request.get_json()
    
    dados=resposta['livro']
    print(dados)
    
    result=db_consulta.pesquisar_livro(dados)
    return  result
    
    
   
   

@app.route("/RegistraLivro",methods=['POST'])
def L1ivro():
    livro=request.get_json()
    register=livro['livro']
    response=db_consulta.cadastrar_livro(register)
   
    return response

    
@app.route("/livroDisponivel")
def Livro():
    resposta=db_consulta.livro_em_stock()
    
    return resposta
    
    
     

app.run(host='0.0.0.0',debug=True)



