import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class SqlHandler:
    def __init__(self) -> None:
        try:
            config = self.get_info_from_env()
            if not config:
                raise Exception('Erro ao carregar variáveis de ambiente')
            self.connection = mysql.connector.connect(host=config['host'],
                                                      port=config['port'],
                                                      database=config['database'],
                                                      user=config['user'],
                                                      password=config['password'])
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
        except Error as e:
            print("Error while connecting to MySQL", e)

    @staticmethod
    def get_info_from_env():
        try:
            load_dotenv()
            return {
                'host': os.getenv('host', '10.28.2.15'),
                'port': os.getenv('port', '3306'),
                'database': os.getenv('database', 'pythonapps'),
                'user': os.getenv('user', 'suporte'),
                'password': os.getenv('password', 'suporte')
            }
        except Exception as e:
            print(f'Erro ao carregar variáveis de ambiente: {e}')
            return False

    def exec_query(self, query, params=None, commit=False):
        if not self.connection.is_connected():
            print("Não conectado ao banco de dados!")
            return False
        
        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            if not commit:
                records = cursor.fetchall()
                return records
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(e)
            return False
        finally:
            cursor.close()