from mysql.connector import connect, Error, errorcode
from decouple import config


class DataBase:
    def __init__(self):
        self.conexion = {
            'user': config('DB_USER'),
            'password': config('DB_PASS'),
            'host': config('DB_HOST'),
            'database': config('DB_NAME'),
            'port': config('DB_PORT')
        }

    def consulta(self, consulta):

        try:
            with connect(**self.conexion) as conexion:
                with conexion.cursor(buffered=True) as cursor:
                    cursor.execute(consulta)

                    if consulta.upper().startswith('SELECT'):
                        data = cursor.fetchall()
                    else:
                        conexion.commit()
                        data = None
                return data
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('E nombre de usuario o la contraseña son incorrectos')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('La base de datos no existe')
            else:
                print(err)
