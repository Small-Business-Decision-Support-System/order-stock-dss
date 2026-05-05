
ALTER TABLE Products ADD COLUMN SafetyStock INT;
ALTER TABLE Products ADD COLUMN DynamicROP INT;
ALTER TABLE Products ADD COLUMN CategoryMatrix VARCHAR(10);


UPDATE Products 
SET CurrentStock = 85, DynamicROP = 93, SafetyStock = 37, CategoryMatrix = 'B-X' 
WHERE ProductName = 'White Sugar 1kg';

UPDATE Products 
SET CurrentStock = 60, DynamicROP = 15, SafetyStock = 5, CategoryMatrix = 'A-X' 
WHERE ProductName = 'Salt 750g';


UPDATE Products 
SET CurrentStock = 20, DynamicROP = 25, SafetyStock = 12, CategoryMatrix = 'C-Z' 
WHERE ProductName = 'Butter 250g';