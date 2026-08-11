SELECT 
    ti.tconst,
    ti.primaryTitle,
    ti.titleType,
    CAST(ti.startYear AS INTEGER) AS startYear,
    CASE WHEN ti.runtimeMinutes = '\N' THEN NULL ELSE CAST(ti.runtimeMinutes AS INTEGER) END AS runtimeMinutes,
    cast(ra.averageRating AS FLOAT) AS averageRating,
    CAST(ra.numVotes AS INTEGER) AS numVotes,
    case WHEN ti.genres = '\N' THEN NULL ELSE ti.genres END AS genres
FROM title_basics ti
JOIN title_ratings ra ON ti.tconst = ra.tconst
WHERE ti.titleType = 'movie' 
    AND ti.isAdult = 0 
    AND ti.startYear != '\N'
ORDER BY cast(startYear AS INTEGER) ASC
LIMIT 20;