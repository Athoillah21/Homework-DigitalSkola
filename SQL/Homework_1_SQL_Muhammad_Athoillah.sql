--QUIZ SQL oleh Muhammad Atho'illah


-- DDL: ref_customers
CREATE TABLE ref_customers (
	cust_id INTEGER,
	cust_nm VARCHAR,
	
	PRIMARY KEY (cust_id)
);

-- DDL: ref_products
CREATE TABLE ref_products (
    prd_id INTEGER,
    prd_nm VARCHAR,
    PRIMARY KEY (prd_id)
);


-- DDL: trx_transactions
CREATE TABLE trx_transactions (
    trx_id INTEGER,
    cust_id INTEGER,
    prd_id INTEGER,
    qty INTEGER,
    price INTEGER,
	PRIMARY KEY (trx_id),
    FOREIGN KEY (cust_id) REFERENCES ref_customers(cust_id) ON DELETE CASCADE,
    FOREIGN KEY (prd_id) REFERENCES ref_products(prd_id) ON DELETE CASCADE
);



--Add ref_customers
INSERT INTO quiz_sql.ref_customers(cust_id,cust_nm) VALUES
(1,'Marzuq'),
(2,'Markus');

-- Check ref_customers
SELECT *
FROM quiz_sql.ref_customers;

--Add ref_products
INSERT INTO quiz_sql.ref_products(prd_id,prd_nm) VALUES
(1,'ABC'),
(2,'XYZ'),
(3,'QWE');

-- Check ref_products
SELECT *
FROM quiz_sql.ref_products;

--Add trx_transactions
INSERT INTO quiz_sql.trx_transactions (trx_id,cust_id,prd_id,qty,price) VALUES
(1,1,1,10,30000),
(2,1,2,20,20000),
(3,1,3,5,10000),
(4,2,1,5,15000),
(5,2,2,5,1000);

-- Check trx_transactions
SELECT *
FROM quiz_sql.trx_transactions;


-- Soal No 1. Berapa produk yang dibeli tiap orang
SELECT c.cust_nm, sum(t.qty) as qty
FROM ref_customers AS c
LEFT JOIN trx_transactions AS t
ON c.cust_id = t.cust_id
GROUP BY cust_nm;

-- Soal N0 2. Berapa Keuntungan Produk ABC
SELECT p.prd_nm, sum(t.price) AS price
FROM ref_products AS p
LEFT JOIN trx_transactions AS t
ON p.prd_id = t.prd_id
WHERE prd_nm = 'ABC'
GROUP BY prd_nm;