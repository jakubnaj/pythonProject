from flask.ext.mysql import MySQL

class MySqlConfig:
    mysql = MySQL()

    def initDatabase(app):
        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'admin123'
        app.config['MYSQL_DATABASE_DB'] = 'adwisedb'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'

        MySqlConfig.mysql.init_app(app)
