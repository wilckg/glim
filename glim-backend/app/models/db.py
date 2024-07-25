from flask import Flask, current_app
import mysql.connector
import bcrypt

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  # ou 'localhost' se estiver na mesma máquina
    'database': 'memori',
}

class Database:
    
    def __init__(self, app: Flask):
        self.app = app
        self.conn = None
        
    def connect(self):
        try:
            self.conn = mysql.connector.connect(**config)
            print("Conexão ao MySQL foi bem-sucedida!")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao MySQL: {err}")
    
    def disconnect(self):
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()
            print("Conexão ao MySQL foi fechada.")
    
    def getUsers(self):
        self.connect()
        
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users')
            results = cursor.fetchall()
            cursor.close()
            return results
        except mysql.connector.Error as err:
            print(f"Erro ao executar a consulta: {err}")
            return []
        finally:
            self.disconnect()  # Fecha a conexão após a operação
    
    def getUserById(self, user_id):
        self.connect()
        
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f"Erro ao executar a consulta: {err}")
            return None
        finally:
            self.disconnect()
            
    def addUser(self, user_data):
        self.connect()
        
        try:
            hashed_password = bcrypt.hashpw(user_data['senha'].encode('utf-8'), bcrypt.gensalt())
            
            cursor = self.conn.cursor()
            query = """
            INSERT INTO users (nome, usuario, senha, status, admin)
            VALUES (%(nome)s, %(usuario)s, %(senha)s, %(status)s, %(admin)s)
            """
            user_data['senha'] = hashed_password.decode('utf-8')
            cursor.execute(query, user_data)
            self.conn.commit()
            cursor.close()
            print("Usuário adicionado com sucesso!")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao inserir usuário: {err}")
            return False
        finally:
            self.disconnect()
            
    def updateUser(self, user_id, user_data):
        self.connect()
        
        try:
            cursor = self.conn.cursor()
            query = """
            UPDATE users
            SET nome = %(nome)s, usuario = %(usuario)s, senha = %(senha)s, status = %(status)s, admin = %(admin)s
            WHERE id = %(id)s
            """
            user_data['id'] = user_id
            
            if 'senha' in user_data:
                hashed_password = bcrypt.hashpw(user_data['senha'].encode('utf-8'), bcrypt.gensalt())
                user_data['senha'] = hashed_password.decode('utf-8')
            
            cursor.execute(query, user_data)
            self.conn.commit()
            cursor.close()
            print(f"Dados do usuário ID {user_id} atualizados com sucesso!")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar dados do usuário: {err}")
            return False
        finally:
            self.disconnect()
            
    def deleteUser(self, user_id):
        self.connect()
        
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            self.conn.commit()
            cursor.close()
            print(f"Usuário ID {user_id} excluído com sucesso!")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar dados do usuário: {err}")
            return False
        finally:
            self.disconnect()