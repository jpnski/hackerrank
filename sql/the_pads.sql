/*  
SUBSTR with position and quantity of characters to select first letter
|| operator to output the name, with parentheses, and the first letter
GROUP BY and ORDER BY to sort sums alphabetically
*/

SELECT
Name || '(' || SUBSTR(Occupation,1,1) || ')'
FROM OCCUPATIONS
ORDER BY Name; 

SELECT
'There are a total of ' || COUNT(Occupation) || ' ' || LOWER(Occupation) || 's.'
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation;
