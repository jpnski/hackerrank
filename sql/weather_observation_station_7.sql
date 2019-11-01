/* []$ for end of string characters */

SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(LOWER(CITY), '[aeiou]$');
