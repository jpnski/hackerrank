/*  ^[] and []$ for first and last character */

SELECT DISTINCT CITY FROM STATION WHERE NOT REGEXP_LIKE(LOWER(CITY), '^[aeiou]') AND NOT REGEXP_LIKE(LOWER(CITY), '[aeiou]$');
