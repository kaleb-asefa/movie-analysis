from sqlalchemy import create_engine, inspect, MetaData, Table, func, select

metadata = MetaData()

engine = create_engine('sqlite:///imdb.db')

print(inspect(engine).get_table_names())

name_basics = Table('name_basics', metadata, autoload_with=engine)
title_basics = Table('title_basics', metadata, autoload_with=engine)
title_crew = Table('title_crew', metadata, autoload_with=engine)
title_ratings = Table('title_ratings', metadata, autoload_with=engine)

print(title_basics.columns.keys())

#deleting all with a titletype not moive
stmt = title_basics.delete().where(title_basics.c.titleType != 'movie')


with engine.connect() as conn:
     result = conn.execute(stmt)
     print(result.rowcount, "rows deleted.")
