from common.MySqlConfig import MySqlConfig
from common.JsonParser import JsonParser


class BaseModel:
    mysql = MySqlConfig.mysql

    def baseRequest(self, query, *args):
        conn = BaseModel.mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query.format(*args))
        results = JsonParser.parseToJson(cursor)
        conn.commit()
        cursor.close
        conn.close
        return results
