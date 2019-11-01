/*  ^[] and []$ for beginning and last character */

SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(LOWER(CITY), '^[aeiou]') AND REGEXP_LIKE(LOWER(CITY), '[aeiou]$');
