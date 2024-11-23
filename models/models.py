import  sqlite3 as  Sq

import  os

class  db_consulta():
    def __iter__(self) :
        pass
    @classmethod
    def cadastrar_livro(cls , livro):
       
            sql = sql = f"INSERT INTO  LIVRO (name) VALUES ('{livro}');"
            database = Sq.connect('dm.db')
            cursor = database.execute(sql)
            database.commit()

          
            database.close()

            return   f"{cursor.rowcount} registro(s) inserido(s)."

       
    @classmethod
    def iniciar_login(cls,senha,email) :

        database = Sq.connect('dm.db')
        sql=f"SELECT  id ,name FROM USER WHERE pass=='{senha}' and email=='{email}' "
        cursor=database.cursor()
        cursor.execute(sql)
        dados=cursor.fetchall()
        database.close()
        if dados==[]:
             return {"info":"acesso  negado"}
        else:
          return  dados
    @classmethod
    def pesquisar_livro(cls,livro):
        database = Sq.connect('dm.db')
        sql=f"SELECT  id ,name  FROM LIVRO WHERE name=='{livro}'"
        cursor=database.cursor()
        cursor.execute(sql)
        dados=cursor.fetchall()
        database.close()
        if dados==[]:
             return {"info":" livro nao encontrado "}
        else:
          return  dados
    @classmethod    
    def livro_em_stock(cls):
        database = Sq.connect('dm.db')
        sql=f"SELECT  id ,name  FROM  LIVRO"
        cursor=database.cursor()
        cursor.execute(sql)
        dados=cursor.fetchall()
        database.close()
        if dados==[]:
             return {"info":" livro nao encontrado "}
        else:
          return  dados
        
    
    
livro="GPL"
#print(db_consulta.cadastrar_livro(livro))



    




    
    




        
        
    
    
        
    