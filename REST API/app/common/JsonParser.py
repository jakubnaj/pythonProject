class JsonParser:
    def parseToJson(cursor):
        """Returns all rows from a cursor as a list of dicts"""
        desc = cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()]
