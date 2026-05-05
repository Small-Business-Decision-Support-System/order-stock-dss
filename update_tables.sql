ALTER TABLE Products -- (Kendi tablonuzun adı neyse onu kullanın: Urunler, Stok vb.)
ADD SafetyStock INT,          -- U Sütunu için (Emniyet Stoğu)
ADD DynamicROP INT,           -- V Sütunu için (Dinamik ROP)
ADD CategoryMatrix VARCHAR(5); -- W Sütunu için (ABC-XYZ Matrisi)