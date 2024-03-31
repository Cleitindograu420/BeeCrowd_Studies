SELECT p.name, po.name 
FROM products p INNER JOIN providers as po  ON p.id_providers = po.id
WHERE p.id_categories = 6;
