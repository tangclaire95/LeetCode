# DISTINCT -- here we use distinct to ensure each author is listed only once even if they have seen multiple of their own articles

SELECT DISTINCT author_id AS id FROM Views 
WHERE author_id = viewer_id 
order BY id ASC; 
