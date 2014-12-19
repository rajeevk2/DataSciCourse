----------------------------------------------------------------------------------------------------
-- PROBLEM 1
----------------------------------------------------------------------------------------------------
select count(1) from frequency -- sample

select count(1) from frequency where docid='10398_txt_earn' -- Problem 1 (a) 110

select * from frequency where docid='10398_txt_earn' and count=1 -- problem 1 (b) 110

-- problem 1 (c) --324 without all, 335 with all
select term from frequency where docid='10398_txt_earn' and count=1 
union all
select term from frequency where docid='925_txt_trade' and count=1 -- 225

-- problem 1 (d)
select count(1) from frequency where term='parliament' -- 15
-- problem 1 (e) -- 11 documents
select count(1) from (select docid from frequency group by docid having count(docid)>=300 ) x
--problem 1 (f) -- 213 rows
select count(1) from ( select docid from frequency where term in ('transactions','world') ) x
----------------------------------------------------------------------------------------------------
-- PROBLEM 1 ENDS
----------------------------------------------------------------------------------------------------