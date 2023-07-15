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
