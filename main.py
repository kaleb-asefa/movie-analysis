from sqlalchemy import create_engine, inspect, MetaData, Table, func, select

metadata = MetaData()

engine = create_engine('sqlite:///imdb.db')

# print(inspect(engine).get_table_names())

name_basics = Table('name_basics', metadata, autoload_with=engine)
title_basics = Table('title_basics', metadata, autoload_with=engine)
title_crew = Table('title_crew', metadata, autoload_with=engine)
title_ratings = Table('title_ratings', metadata, autoload_with=engine)

for col in title_ratings.columns:
    print(col.name, col.type)