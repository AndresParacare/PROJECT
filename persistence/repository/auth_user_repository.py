import sqlalchemy as db
from persistence.model import Auth_User
from sqlalchemy.orm import Session

#Clase que se encarga de la autenticación de usuarios
class AuthUserRepository():
    
    #abre la conexión a la base de datos
    def __init__(self):
        self.engine = db.create_engine('sqlite:///db/login.sqlite',
                                       echo=False, future=False)
    
    #Verifica si el usario exite
    #Tambien verifica si el usuario y contraseña son correctos
    def getUserByUserName(self, user_name: str):
        user: Auth_User = None
        with Session(self.engine) as session:
            user = session.query(Auth_User).filter_by(
                user_name = user_name).first()
        return user
    
    #Insertaer un usuario a la base de datos
    def insertUser(self, user: Auth_User):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
