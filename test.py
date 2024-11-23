from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar o banco de dados
engine = create_engine('sqlite:///meu_banco.db')
Base = declarative_base()

# Definir a tabela
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', email='{self.email}')>"

# Criar a tabela no banco de dados
Base.metadata.create_all(engine)

# Criar sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionar um novo registro
novo_usuario = Usuario(nome="Ana", email="ana@example.com")
session.add(novo_usuario)
session.commit()

# Consultar registros
usuarios = session.query(Usuario).all()
print(usuarios)
