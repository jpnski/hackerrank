/*
ROW_NUMBER()
OVER()
PARTITION()
PIVOT()
*/

SELECT Doctor, Professor, Singer, Actor
FROM (
    SELECT ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) as rn, Name, Occupation
    FROM OCCUPATIONS)
PIVOT
(
MIN(Name)
FOR Occupation
IN ('Doctor' as Doctor, 'Professor' as Professor, 'Singer' as Singer, 'Actor' as Actor)
)
ORDER BY rn;
