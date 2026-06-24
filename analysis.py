from sqlalchemy import select
from main import title_basics, title_ratings, title_crew, name_basics, engine
from tabulate import tabulate

stmt = select(title_basics.c.primaryTitle, title_basics.c.startYear, 
                           title_ratings.c.averageRating).join(title_ratings, title_basics.c.tconst == title_ratings.c.tconst).where(
                               title_ratings.c.averageRating > 8.0).order_by(title_ratings.c.averageRating.desc()).limit(10)

stmt2 = title_ratings.select().limit(10)

with engine.connect() as conn:
    result = conn.execute(stmt)
    headers = result.keys()
    rows = result.fetchall()
    print(tabulate(rows, headers=headers, tablefmt='grid'))
