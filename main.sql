SELECT 
    ti.tconst AS id,
    ti.primaryTitle AS title,
    CAST(ti.startYear AS INTEGER) AS year,
    CASE WHEN ti.runtimeMinutes = '\N' THEN NULL ELSE CAST(ti.runtimeMinutes AS INTEGER) END AS runtimeMinutes,
    cast(ra.averageRating AS FLOAT) AS rating,
    CAST(ra.numVotes AS INTEGER) AS votes,
    case WHEN ti.genres = '\N' THEN NULL ELSE ti.genres END AS genres
FROM title_basics ti
JOIN title_ratings ra ON ti.tconst = ra.tconst
WHERE ti.titleType = 'movie' 
    AND ti.isAdult = 0 
    AND ti.startYear != '\N'
ORDER BY cast(startYear AS INTEGER) ASC
