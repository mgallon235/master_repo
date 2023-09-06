
----View database tables (highlevel)
select table_schema, table_name
from information_schema.tables;


----Check columns and data types
select table_name, column_name, data_type
from information_schema.columns
where table_schema = 'public'
order by table_name, ordinal_position;


-----Creating a new table
Create Table test_2(
id numeric,
name text,
last_name text,
hometown char(24)
);


----- Add new column
alter table test_2
add hometown text;


----- Renaming column
alter table test_2
rename hometown to district;


----- drop column 
alter table test_2
drop column city;


---### Inserting Data to tables + renaming columns ####

insert into test_2
select customer_id, purchase_amount, dates
from sales_table;

--- Drop Table:
drop table test_table;