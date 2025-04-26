from database.DB_connect import DBConnect


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getParole():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT nome FROM parola"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["nome"])

        cursor.close()
        conn.close()
        return result
