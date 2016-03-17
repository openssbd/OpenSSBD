#Installing OpenSSBD on Ubuntu 14.04 
- Install the latest update and install a list of dependency programs

  ```
  # apt-get update
  # apt-get upgrade
  # apt-get install python
  # apt-get install python-numpy
  # apt-get install python-pandas
  # apt-get install python-matplotlib
  # apt-get install postgresql 
  # apt-get install python-django
  # apt-get install git 
  # apt-get install python-defusedxml
  # apt-get install python-tastypie
  # apt-get install python-psycopg2
  # apt-get install postgresql postgresql-contrib
  ```

- Starting PostgreSQL and setting up a new SSBD DB
  - check access to DB by editing `/etc/postgresql/9.3/main/pg_hba.conf`
  ```
  # Database administrative login by Unix domain socket
  local   all             postgres                                trust
  ```
  - Start up PostgreSQL
  ```
  # service postgresql start
  # sudo -i -u postgres
  # psql
  postgres=# create database "SSBD" encoding 'utf8' template template0;
  postgres=# alter user postgres with password 'postgres';
  ```
- Download OpenSSBD code using Git
  1. Change to the directory where you want **OpenSSBD** to reside. The default directory is `/usr/src/OpenSSBD`
  ```
  # mkdir -p /usr/src/OpenSSBD
  # cd /usr/src/OpenSSBD
  ```
  2. Clone OpenSSBD from Github
  ```
  # git clone https://github.com/openssbd/OpenSSBD.git
  ```
- Other Changes need in `/usr/src/OpenSSBD/SSBD/settings.py`
  * if you are not using default directory, you will need to change the variable STATICFILES_DIRS, below is the default setting
  ```
  STATICFILES_DIRS = ('/usr/src/OpenSSBD/SSBD/SSBD/static',)
  ```
- Creating database tables via Django
```
    # cd /usr/src/OpenSSBD/SSBD
    # python manage.py syncdb
```
- Setting up owner model
```
    # psql -h localhost -U postgres -d "SSBD"
    postgres=# insert into "SSBD2_owner_model" (password, last_login, username, email, first_name, is_active, date_joined, phone, "URL", organization, department, laboratory, address) values ('', '2016-01-01 JST', 'public', '', '', TRUE, '2016-01-01 JST', '', '', '', '', '', '');
```
- Defining SQL functions
```
    # cd /usr/src/OpenSSBD/SSBD/Tools
    # psql -h localhost -U postgres -d "SSBD" -f unicoords.sql 
    # psql -h localhost -U postgres -d "SSBD" -f stat.sql     
    # psql -h localhost -U postgres -d "SSBD" -f gen_compstat.sql
    # psql -h localhost -U postgres -d "SSBD" -f schemaUpdate4.sql 
```
- Start up OpenSSBD 
```
    # cd /usr/src/OpenSSBD/SSBD
    # python manage.py runserver 0:8282
```
- OpenSSBD can now be accessed by a web browser `http://localhost:8282`
