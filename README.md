# OpenSSBD

**OpenSSBD Database Engine - for storing and retrieving quantitative data of biological dynamics**

Copyright (C) 2016  RIKEN/JST

Original contributors: Kenneth H.L. Ho, Yukako Tohsato, Koji Kyoda, Shuichi Onami
    
# Synopsis

**OpenSSBD** is the open-source version of SSBD [Systems Science of Biological Dynamics] (http://ssbd.qbic.riken.jp/) database engine.
This open-source version is mainly created for biologists and others for storing and retrieving quantitative data of biological dynamics. 

[Systems Science of Biological Dynamics (SSBD)](http://ssbd.qbic.riken.jp/) database provides a rich set of resources for analyzing spatiotemporal dynamics of biologcial objects, 
such as single molecules, nuclei, and gene expressed cells. **OpenSSBD** provides the backend database engine for storing and retrieving quantitative biological data which can be collected from a variety of species, sources and methods. 
Quantitative numerical data are represented in a new Biological Dynamics Markup Language (BDML). The new data format allows users to exchange, store, compare and analyze data through the OpenSSBD database engine.

## Reference
Koji Kyoda, Yukako Tohsato, Kenneth H. L. Ho, Shuichi Onami (2015),
Biological Dynamics Markup Language (BDML): an open format for representing quantitative biological dynamics data. Bioinformatics 31(7): 1044-1052 
<http://bioinformatics.oxfordjournals.org/content/31/7/1044>.

# Screen shot
![Alt text](openssbd_screen.jpg?raw=true "OpenSSBD screenshot")

# Motivation

SSBD (http://ssbd.qbic.riken.jp/) database was developed as an open database for storing and sharing quantitative biological dynamics data. 
With the rapid advance in microscopy, bioimage informatics, there is now a large amount of quantitative data on spatiotemporal dynamics of biological objects ranging from molecules to organisms.  
SSBD aims to facilitate the reuse of these quantitative and imaging data for references and for further analysis.

**OpenSSBD** is released as open source software allowing system biology community and other interested parties to collaborate and to enhance the platform for sharing and reuse of quantitative data of biological dynamics.

# Overview of OpenSSBD
* *OpenSSBD* is a client server based distributed web application. 
* It is written in [Python](https://www.python.org/) using [Django web application framework](https://www.djangoproject.com/) and [PostgreSQL](http://www.postgresql.org/) database engine. 
* RESTful API is written using [Tastypie API framework for Django](https://django-tastypie.readthedocs.org/en/latest/)
* Browser based visualisation is mainly written in Javascript and uses [Three.js](http://threejs.org/) Javascript 3D library and [jQuery](https://jquery.com/)/[jQuery-UI](https://jqueryui.com/) libraries.
![Alt text](OpenSSBD.jpg?raw=true "Overview of OpenSSBD")

# Installation

There are two recommended installation methods:

## Installation using a Docker image
  1. Pre-requisite
     Install docker - https://docs.docker.com/engine/installation/
  2. Get a copy of the image from from Docker Hub 
        ```
        # docker run openssbd/public
        
     1. This image includes OpenSSBD database engine together with 1 dataset ["Quantitative information about nuclear division dynamics in wild-type embryo of _C. elegans_"](http://ssbd.qbic.riken.jp/search/afc304bc-7cca-4c92-8764-f5957dd06e3d/)

        ref: [Koji Kyoda, et al. (2013), WDDD: Worm Developmental Dynamics Database. Nucleic Acids Research 41(Database issue): D732-D737.](http://www.ncbi.nlm.nih.gov/pubmed/23172286)
     
        ```
  3. Examine the image in docker
    ```
     # docker images
    ```
  4. Start the container - mapping and using port 8282
```
# docker run -i -t -p 8282:8282 openssbd/internal:1 /bin/bash
```
Or
```
# docker run -i -t -p 8282:8282 openssbd_serv /bin/bash
```
  5. Setting up within the container
     1. Start up postgresql
       ```
       root@[container]:~/# /etc/init.d/postgresql start
       ```
     2. Start up OpenSSBD 
      ```
      root@[container]:~/# cd /usr/src/OpenSSBD
      root@[container]:/usr/src/OpenSSBD/# python manage.py runserver 0:8282
      ```
  6. OpenSSBD can now be accessed by a web browser http://localhost:8282
     * note: For Windows and MacOS users, you need to find out the IP address of the Docker-Machine using the command below.
     You can then access it on the web browser by using http://[ip address]:8282
       ```
       # docker-machine ip default
       ```

## Installing on Ubuntu 14.04 Linux VM/machine.
  1. Install the latest update and install a list of dependency programs
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
  2. Starting PostgreSQL and setting up a new SSBD DB
     1. check access to DB by editing /etc/postgresql/9.3/main/pg_hba.conf
     ```
          # Database administrative login by Unix domain socket
     local   all             postgres                                trust
     ```
     2. Start up PostgreSQL
   ```
   # service postgresql start
   # sudo -i -u postgres
   # psql
   postgres=# create database "SSBD" encoding 'utf8' template template0;
   postgres=# alter user postgres with password 'postgres';
   ```
  3. Download OpenSSBD code using Git
     1. Change to the directory where you want **OpenSSBD** to reside. The default directory is /usr/src/OpenSSBD
     ```
     # mkdir -p /usr/src/OpenSSBD
     # cd /usr/src/OpenSSBD
     ```
     2. Clone OpenSSBD from Github
     ```
     # git clone https://github.com/openssbd/OpenSSBD.git
     ```
  4. Other Changes need in /usr/src/OpenSSBD/SSBD/settings.py
        * if you are not using default directory, you will need to change the variable STATICFILES_DIRS, below is the default setting
        ```
        STATICFILES_DIRS = ('/usr/src/OpenSSBD/SSBD/SSBD/static',)
        ```
  5. Creating database tables via Django
     ```
     # cd /usr/src/OpenSSBD/SSBD
     # python manage.py syncdb
     ```
  6. Setting up owner model
     ```
     # psql -h localhost -U postgres -d "SSBD"
     postgres=# insert into "SSBD2_owner_model" (password, last_login, username, email, first_name, is_active, date_joined, phone, "URL", organization, department, laboratory, address) values ('', '2016-01-01 JST', 'public', '', '', TRUE, '2016-01-01 JST', '', '', '', '', '', '');
     ```
  7. Defining SQL functions
     ```
     # cd /usr/src/OpenSSBD/SSBD/Tools
     # psql -h localhost -U postgres -d "SSBD" -f unicoords.sql 
     # psql -h localhost -U postgres -d "SSBD" -f stat.sql     
     # psql -h localhost -U postgres -d "SSBD" -f gen_compstat.sql
     # psql -h localhost -U postgres -d "SSBD" -f schemaUpdate4.sql 
     ```
  8. Start up OpenSSBD 
      ```
      # cd /usr/src/OpenSSBD/SSBD
      # python manage.py runserver 0:8282
      ```
  9. OpenSSBD can now be accessed by a web browser http://localhost:8282

# API Reference
1. Details of the API can be found on SSBD main web site <http://ssbd.qbic.riken.jp/restfulapi/>
2. Additional API specific for OpenSSBD

<h2 id="SummaryofAdditionalOpenSSBDAPI">Summary of Additional OpenSSBD API</h2>
<table class="wiki">
<tr><th> <strong>API</strong> </th><th> <strong>Request Method</strong> </th><th> <strong>Functions</strong> </th><th> <strong>Status</strong> 
</th></tr><tr><td style="text-align: left">/SSBD/BDML/read_file/&lt;filename&gt;   </td><td> POST or GET </td><td> Importing BDML file &lt;filename&gt; into OpenSSBD  </td><td> only support BDML v0.15 
</td></tr><tr><td style="text-align: left">/SSBD/BDML/qdb_data/&lt;bdml_id&gt;   </td><td> DELETE </td><td> Deleting dataset &lt;bdml_id&gt;  </td><td> when there is error in importing dataset, this API may not delete the incomplete dataset cleanly 
</td></tr><tr><td style="text-align: left">/SSBD/BDML/vertices/&lt;bdml_id&gt;/t/&lt;timepoint&gt;/etype/&lt;entity type&gt;   </td><td> GET   </td><td> Retrieving coordinates of &lt;bdml_id&gt; at &lt;timepoint&gt; with &lt;entity type&gt;  </td><td> 
</td></tr></table>

## read_file API
  * **Description** - Importing BDML files into OpenSSBD
  * Usage:
  ``` /SSBD/BDML/readfile/<filename>/ ```
    * where filename is the name of the BDML file
    * limit to importing BDML version 0.15 format
    * e.g.
    ```
    # curl -X POST http://localhost:8282/SSBD/BDML/read_file/wt_N2_030131_01.bdml0.15.xml/
    {"details": "bdml 563d487f-1676-4159-a3ab-c25c2e198f6c is saved in the database", "error": "none"}
    ```
    
## qdb_data API
  * **Description** - Deleting dataset in OpenSSBD
  * Usage:
  ``` /SSBD/BDML/qdb_data/<bdml_id>/ ```
    * it requires a DELETE http function
    * where bdml_id is the internal ID of the dataset
    * It may not cleanly delete data when there is importing error
    * e.g.
    ```
    # curl -X DELETE http://localhost:8282/SSBD/BDML/qdb_data/1/
    ```
    
## vertices API 
  * **Description** - Retrieving coordinates from OpenSSBD for displaying on a web browser
  * Usage:
  ``` /SSBD/BDML/vertices/<bdml_id>/t/<time pt>/etype/<entity type>/ ```
    * where bdml_id is the internal ID of the dataset
    * time pt is the data related to the specific time point
    * entity type is the type of entity which one wants to retrieve, point, sphere and line. Face is not supported yet.
    * e.g. retrieving BDML internal ID=1 at time point=10 and enitity type=line 
      ```
      http://localhost:8282/SSBD/BDML/vertices/1/t/10/etype/line/
      ```
    * It will always return in JSON format with a key _vertices_ and a list of coordinates with its component and entity ids
      ```
      { vertices : [entity_id, coordinates_id, x, y, z, t, ... ] }
      ```


# Importing BDML files into OpenSSBD
1. Create a directory in /tmp/bdml 
   ```
   # mkdir -p /tmp/bdml
   ```
2. Copy the bdml files to the /tmp/bdml directory, e.g. 
   ```
    # cp wt_N2_030131_01.bdml0.15.xml /tmp/bdml
    ```
3. Call read_file API, e.g. 
    ```
    # curl -X POST http://localhost:9292/SSBD/BDML/read_file/wt_N2_030131_01.bdml0.15.xml/
    {"details": "bdml 563d487f-1676-4159-a3ab-c25c2e198f6c is saved in the database", "error": "none"}
    ```
4. Find the bdml internal ID number using bdml API, e.g.  
   ```
   http://dhcp20-193.cdb.riken.jp:8282/SSBD/api/v1/bdml/?format=xml;bdml__bdml_ID__icontains=563;
   ```
   * Result:
   ```
<response>
<objects type="list">
<object>
<bdml_ID>563d487f-1676-4159-a3ab-c25c2e198f6c</bdml_ID>
<id type="integer">1</id>
<title>
BDML file for quantitative information about nuclear division dynamics of wild-type embryo
</title>
</object>
</objects>
<meta type="hash">
<next type="null"/>
<total_count type="integer">1</total_count>
<previous type="null"/>
<limit type="integer">20</limit>
<offset type="integer">0</offset>
</meta>
</response>
```
5. Update the root table via SQL function schemaupdate4 together with the internal ID number 
  * e.g.
```
psql -h localhost -U postgres -d "SSBD" -c "select schemaupdate4(1);"
NOTICE:  Inserted 1 into SSBD2_meta_data_model
NOTICE:  Inserted 1 into SSBD2_quant_data_model
NOTICE:  Inserted 1 into SSBD2_scaleunit_data_model
NOTICE:  Inserted 1 into SSBD2_bml_multipart_model
NOTICE:  Inserted 1 into SSBD2_root_data_model
 schemaupdate4 
---------------
             1
(1 row)
```
6. Update the unicoords table via SQL function unicoords - it fills in the entries by calculating all the coordinates in micrometers.
  * e.g.
```
# psql -h localhost -U postgres -d "SSBD" -c "select unicoords(1);"
NOTICE:  Starting to insert 1 into SSBD
NOTICE:  Inserted 1 into SSBD
 unicoords 
-----------
         1
(1 row)
```
7. Updating statistical table via function genstats
  * e.g.
```
# psql -h localhost -U postgres -d "SSBD" -c "select genstats(1);"
NOTICE:  Starting to insert stats 1 into SSBD
NOTICE:  Inserted stats 1 into SSBD
 genstats 
----------
        1
(1 row)
```

# Differences between OpenSSBD and SSBD
* Although [SSBD](http://ssbd.qbic.riken.jp) is currently running on [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) servers, OpenSSBD is built on top of [Ubuntu](http://www.ubuntu.com/) 14.04 Linux.
* It does not include OMERO image database. Users will need to install OMERO separately. (see https://www.openmicroscopy.org/site for more details)
* Functions are limited to
  * Importing BDML 0.15 files including data types for points, lines and spheres, but not face.
  * Importing BDML files does not support multi-part BDML files
  * Browser visualisation is limited to single time-point viewer as multiple time point viewer requires special manually tweeted optimizations
  * CSS style file is not included as it contains 3rd parties copyright material.
* read_file API is included in OpenSSBD for importing BDML files.  
  * It is not available to the public on SSBD. It is a privileged function to import BDML files into SSBD.

# Known issues
* Importing data is done manually through command line.
* There is only a limit basic function to delete a dataset and may need to manually remove entry from the SQL DB.
* Function to update a dataset is not provided. This is due to fact that any change to a BDML file would require creating a new unique BDML file with a unique BDML_ID. Instead there is a provision in SQL table to label a dataset status, e.g. available, error, etc.
* Although there is a provision in the root table to allow different meta information to be stored without re-importing the same dataset, data has to be updated manually.
* There is no automated function to input or update the location of the BDML files. Those data have to be input manually into the SQL tables.

# Contributors guide
* Please feel free to fork, enhance/modify OpenSSBD. We look forward to hearing from you and together we hope to share new ideas and collaborate in new projects using OpenSSBD.
* If you find any bugs, or questions, please submit and open an Issue. 

# Acknowledgment
This work has been partly supported by National Bioscience Database Center (NBDC) of Japan Science and Technology Agency (JST).

# License

Copyright (C) 2016  RIKEN/JST

GNU GENERAL PUBLIC LICENSE  Version 3 (GPLv3.0)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
