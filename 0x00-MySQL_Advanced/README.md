# 0x00. MySQL advanced
## Requirements
### General
-   All your files will be executed on Ubuntu 18.04 LTS using  `MySQL 5.7`  (version 5.7.30)
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`…)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`

### How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Tasks

### 0. We are all unique!
Files:  [0-uniq_users.sql](0-uniq_users.sql)

Write a SQL script that creates a table  `users`  following these requirements:

-   With these attributes:
    -   `id`, integer, never null, auto increment and primary key
    -   `email`, string (255 characters), never null and unique
    -   `name`, string (255 characters)
-   If the table already exists, your script should not fail
-   Your script can be executed on any database

```
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 
```


### 1. In and not out
Files:  [1-country_users.sql](1-country_users.sql)

Write a SQL script that creates a table  `users`  following these requirements:

-   With these attributes:
    -   `id`, integer, never null, auto increment and primary key
    -   `email`, string (255 characters), never null and unique
    -   `name`, string (255 characters)
    -   `country`, enumeration of countries:  `US`,  `CO`  and  `TN`, never null (= default will be the first element of the enumeration, here  `US`)
-   If the table already exists, your script should not fail
-   Your script can be executed on any database

```
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$ 
```

### 2. Best band ever!
Files:  [2-fans.sql](2-fans.sql)

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**
-   Import this table dump:  [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ "metal_bands.sql.zip")
-   Column names must be:  `origin`  and  `nb_fans`
-   Your script can be executed on any database

**Context:**  _Calculate/compute something is always power intensive… better to distribute the load!_

```
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$ 
```

### 3. Old school band
Files:  [3-glam_rock.sql](3-glam_rock.sql)

Write a SQL script that lists all bands with  `Glam rock`  as their main style, ranked by their longevity

**Requirements:**
-   Import this table dump:  [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ "metal_bands.sql.zip")
-   Column names must be:  `band_name`  and  `lifespan`  (in years  **until 2022**  - please use  `2022`  instead of  `YEAR(CURDATE())`)
-   You should use attributes  `formed`  and  `split`  for computing the  `lifespan`
-   Your script can be executed on any database

```
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$ 
```

### 4. Buy buy buy
File:  [4-store.sql](4-store.sql), [4-init.sql](4-init.sql), [4-main.sql](4-main.sql)

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table  `items`  can be negative.

**Context:**  _Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!_

```
bob@dylan:~$ 
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item_name   number
apple   1
apple   3
pear    2
bob@dylan:~$ 
```

### 5. Email validation to sent
File:  [enter link description here](5-valid_email.sql), [5-init.sql](5-init.sql), [5-main.sql](5-main.sql)

Write a SQL script that creates a trigger that resets the attribute  `valid_email`  only when the  `email`  has been changed.

**Context:**  _Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!_

```
bob@dylan:~$ 
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton 
Enter password: 
id  email   name    valid_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$ 
```

### 6. Add bonus
File:  [6-bonus.sql](6-bonus.sql), [6-init.sql](6-init.sql), [6-main.sql](6-main.sql)

Write a SQL script that creates a stored procedure  `AddBonus`  that adds a new correction for a student.

**Requirements:**
-   Procedure  `AddBonus`  is taking 3 inputs (in this order):
    -   `user_id`, a  `users.id`  value (you can assume  `user_id`  is linked to an existing  `users`)
    -   `project_name`, a new or already exists  `projects`  - if no  `projects.name`  found in the table, you should create it
    -   `score`, the score value for the correction

**Context:**  _Write code in SQL is a nice level up!_

```
bob@dylan:~$ 
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name
1   C is fun
2   Python is cool
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$ 
```

### 7. Average score
File:  [7-average_score.sql](7-average_score.sql) , [7-init.sql](7-init.sql), [7-main.sql](7-main.sql)

Write a SQL script that creates a stored procedure  `ComputeAverageScoreForUser`  that computes and store the average score for a student. Note: An average score can be a decimal

**Requirements:**

-   Procedure  `ComputeAverageScoreForUser`  is taking 1 input:
    -   `user_id`, a  `users.id`  value (you can assume  `user_id`  is linked to an existing  `users`)

```
bob@dylan:~$ 
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-average_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$ 
```

### 8. Optimize simple search
File:  [8-index_my_names.sql](8-index_my_names.sql)

Write a SQL script that creates an index  `idx_name_first`  on the table  `names`  and the first letter of  `name`.

**Requirements:**

-   Import this table dump:  [names.sql.zip](https://intranet.alxswe.com/rltoken/BluyCCIIfw0NqcjqUiUdEw "names.sql.zip")
-   Only the first letter of  `name`  must be indexed

**Context:**  _Index is not the solution for any performance issue, but well used, it’s really powerful!_

```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 8-index_my_names.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql> 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 
```

### 9. Optimize search and score
File:  [9-index_name_score.sql](9-index_name_score.sql)

Write a SQL script that creates an index  `idx_name_first_score`  on the table  `names`  and the first letter of  `name`  and the  `score`.

**Requirements:**

-   Import this table dump:  [names.sql.zip](https://intranet.alxswe.com/rltoken/BluyCCIIfw0NqcjqUiUdEw "names.sql.zip")
-   Only the first letter of  `name`  AND  `score`  must be indexed

```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 9-index_name_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name             | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx_name_first_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql> 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 
```

### 10. Safe divide
File:  [10-div.sql](10-div.sql), [10-init.sql](10-init.sql)

Write a SQL script that creates a function  `SafeDiv`  that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

**Requirements:**

-   You must create a function
-   The function  `SafeDiv`  takes 2 arguments:
    -   `a`, INT
    -   `b`, INT
-   And returns  `a / b`  or 0 if  `b == 0`

```
bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$ 
```

### 11. No table for a meeting
File:  [11-need_meeting.sql](11-need_meeting.sql), [11-init.sql](11-init.sql), [11-main.sql](11-main.sql)

Write a SQL script that creates a view  `need_meeting`  that lists all students that have a score under 80 (strict) and no  `last_meeting`  or more than 1 month.

**Requirements:**

-   The view  `need_meeting`  should return all students name when:
    -   They score are under (strict) to 80
    -   **AND**  no  `last_meeting`  date  **OR**  more than a month

```
bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-need_meeting.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password: 
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character_set_client    collation_connection
XXXXXX<yes, here it will display the View SQL statement :-) >XXXXXX
--
--
Table   Create Table
students    CREATE TABLE `students` (\n  `name` varchar(255) NOT NULL,\n  `score` int(11) DEFAULT '0',\n  `last_meeting` date DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$ 
```
### 12. Average weighted score
File:  [100-average_weighted_score.sql](100-average_weighted_score.sql), [100-init.sql](100-init.sql), [100-main.sql](100-main.sql)

Write a SQL script that creates a stored procedure  `ComputeAverageWeightedScoreForUser`  that computes and store the average weighted score for a student.

**Requirements:**

-   Procedure  `ComputeAverageScoreForUser`  is taking 1 input:
    -   `user_id`, a  `users.id`  value (you can assume  `user_id`  is linked to an existing  `users`)

**Tips**:

-   [Calculate-Weighted-Average](https://intranet.alxswe.com/rltoken/QHx92mlF43zF6GTEil-Cyw "Calculate-Weighted-Average")
```
bob@dylan:~$ 
bob@dylan:~$ cat 100-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 100-average_weighted_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 100-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  82
id  name    weight
1   C is fun    1
2   Python is cool  2
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
id  name    average_score
1   Bob 0
2   Jeanne  79
bob@dylan:~$ 
```

### 13. Average weighted score for all!
File:  [101-average_weighted_score.sql](101-average_weighted_score.sql), [101-main.sql](101-main.sql), [101-init.sql](101-init.sql)

Write a SQL script that creates a stored procedure  `ComputeAverageWeightedScoreForUsers`  that computes and store the average weighted score for all students.

**Requirements:**

-   Procedure  `ComputeAverageWeightedScoreForUsers`  is not taking any input.

**Tips**:

-   [Calculate-Weighted-Average](https://intranet.alxswe.com/rltoken/QHx92mlF43zF6GTEil-Cyw "Calculate-Weighted-Average")

```
bob@dylan:~$ cat 101-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 101-average_weighted_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 101-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
id  name    weight
1   C is fun    1
2   Python is cool  2
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
id  name    average_score
1   Bob 90.6667
2   Jeanne  79
bob@dylan:~$ 
```

> Written with [StackEdit](https://stackedit.io/).
