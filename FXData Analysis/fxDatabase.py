from sqlalchemy import create_engine, Float
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


# Global Variable
SQLITE = 'sqlite'

#Table Name
FXDATA = 'fxdata'

class FXDatabase:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE : 'sqlite:///{DB}',
    }

    #Main DB connection ref obj
    db_engine = None

    def __init__(self, dbtype, username='', password = '', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)

            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in the database")

    def create_db_tables(self):
        metadata = MetaData()
        users = Table(FXDATA, metadata,
                      Column('id',Integer, primary_key=True),
                      Column('time', String),
                      Column('FXRate', Float),
                      Column('EntryTime', String)
                      )
        try:
            metadata.create_all(self.db_engine)
            print('Table Created')
        except Exception as e:
            print('Error occurred during Table creation.')
            print(e)

    # Insert, Update, Delete
    def execute_query(self, query = ''):
        if query == '':
            return
        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * from '{}';".format(table)
        print(query)

        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row) #print row #0, row #1, row #2
                    result.close()
        print('\n')




