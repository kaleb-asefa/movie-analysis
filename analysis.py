from sqlalchemy import select, and_, func, cast, Integer
from main import title_basics, title_ratings, title_crew, name_basics, engine
from tabulate import tabulate
import pickle
import numpy as np
import pandas as pd

stmt = select(title_basics.c.primaryTitle, title_basics.c.startYear, title_basics.c.genres,title_ratings.c.averageRating, title_ratings.c.numVotes).join(
                title_ratings, title_basics.c.tconst == title_ratings.c.tconst).where(and_(title_basics.c.titleType == 'movie',
                cast(title_ratings.c.numVotes, Integer) > 20000,
                title_basics.c.genres.notlike('%Adult%'), title_basics.c.genres.notlike('%Documentary%'), 
                title_basics.c.genres.notlike('%Short%'))).order_by(title_ratings.c.averageRating.desc())


with engine.connect() as conn:
    result = conn.execute(stmt).fetchall()
    df = pd.DataFrame(result, columns=['Title', 'Year', 'Genres', 'Rating', 'Votes'])
    df.to_csv('top_movies.csv', index=False)
    



