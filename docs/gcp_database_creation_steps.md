# GCP database creation steps
1. Go to the GCP console -> Cloud SQL -> Create instance
    1.1. Select database engine, in this case I'll be using PostgreSQL  
    1.2. Set the instance id  
    1.3. Set the password or let google generate it (make sure to save the password safely)  
    1.4. Se the region to the same as the region used in the project (for this project is us-central1)

2. Once the instance is created we can proceed to create the database  
    2.1. Go to the created instance Instances -> created instance   
    2.2. Go to Databases -> Create database  
    2.3. Insert the database name, in this case `gcp_database`  

3. Create roles for the database  
    3.1 Go to Users -> Add user account  
    3.2 Set the user name  
    3.3 Set the password  
    3.4 

4. Set the connection to the database
    4.1 Install psql (if we want to connect to the database locally) `sudo apt install postgresql-client`  
    4.2 `gcloud sql connect <instance>  \
  --user=<user> \
  --database=<database>`

5. Once the role is created and the connection is set we can manage the database as we would usually do with any database connection through console

---

# Example of management for the database 

Create database

``` sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Insert into the database some random user

``` sql
INSERT INTO users (name, email)
VALUES ('Pablo Coti', 'pca2003gte@gmail.com');
```

List the data from `users` table

``` sql
SELECT * FROM users;
```

