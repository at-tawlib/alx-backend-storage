# 0x01. NoSQL

`Back-end` --  `NoSQL` -- `MongoDB`

## Requirements


### Python Scripts

-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  `python3`  (version 3.7) and  `PyMongo`  (version 3.10)
-   Your code should use the  `pycodestyle`  style (version 2.5.*)
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
-   Your code should not be executed when imported (by using  `if __name__ == "__main__"`:)


###  Tasks
[0-list_databases](0-list_databases) :  lists all databases in MongoDB.
```
guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
```

[1-use_or_create_database](1-use_or_create_database) : creates or uses the database  `my_db`:
```
guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
guillaume@ubuntu:~/0x01$ cat 1-use_or_create_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
guillaume@ubuntu:~/0x01$
```

[2-insert](2-insert) : inserts a document in the collection  `school`:

-   The database name will be passed as option of  `mongo`  command

```
guillaume@ubuntu:~/0x01$ cat 2-insert | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
guillaume@ubuntu:~/0x01$
```

[3-all](3-all) :  lists all documents in the collection  `school`:
-   The database name will be passed as option of  `mongo`  command

```
guillaume@ubuntu:~/0x01$ cat 3-all | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```

[4-match](4-match) :  lists all documents with  `name="Holberton school"`  in the collection  `school`:
-   The database name will be passed as option of  `mongo`  command

```
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```

[5-count](5-count) : displays the number of documents in the collection  `school`:
-   The database name will be passed as option of  `mongo`  command

```
guillaume@ubuntu:~/0x01$ cat 5-count | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
1
bye
guillaume@ubuntu:~/0x01$
```

[6-update](6-update) : adds a new attribute to a document in the collection  `school`:
-   The script should update only document with  `name="Holberton school"`  (all of them)
-   The update should add the attribute  `address`  with the value “972 Mission street”
-   The database name will be passed as option of  `mongo`  command

```
guillaume@ubuntu:~/0x01$ cat 6-update | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
guillaume@ubuntu:~/0x01$ 
```

[7-delete](7-delete) : deletes all documents with  `name="Holberton school"`  in the collection  `school`:
-   The database name will be passed as option of  `mongo`  command

```
guillaume@ubuntu:~/0x01$ cat 7-delete | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "acknowledged" : true, "deletedCount" : 1 }
bye
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
bye
guillaume@ubuntu:~/0x01$ 
```
