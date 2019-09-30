# Report Generator for Log Analysis
This is a intenal reporting tool, Report Generator, for a newspaper site. This project will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

There are four files in this project:
- README.md: README file to get you started running this project
- report_generator.py: the report generator
- report_gen_helper.py: the report generator help function
- create_view.sql: the sql script to create view in the database
- report_example.txt: what you should get after running this project

## Installation 
### Install and Configure Virtual Machine 
Install and configure the VM following the [instruction](https://github.com/udacity/fullstack-nanodegree-vm). 

### Get VM up and running
After navigating to the directory that the VM file are stored, run `vagrant up` and `vagrant ssh` to get the VM up and running. More detail see [Udacity Full Stack VM - start the virtual machine](https://github.com/udacity/fullstack-nanodegree-vm#start-the-virtual-machine)
If you have trouble with VM set up and running, refer to [Udacity Full Stack VM - troubleshooting](https://github.com/udacity/fullstack-nanodegree-vm#start-the-virtual-machine)

## Getting Started
### Import News Database
Import the Database `news` using the following query.
```sh
psql -d news -f newsdata.sql
```

### Create view with postgresql
SQL script used for creating views are included in the create_view.sql file. To run this file and create views in the database, run:
```
psql -d news -f create_views.sql
```

### Run python code
There are two ways of getting the report by running this code. 
- If you want to get the report printed in the terminal, run:
```sh
python3 report_generator.py
```
- If you want to save the report to a txt file, run:
```sh
python3 report_generator.py > report.txt
```

## Supporting Materials
- [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm#full-stack-web-developer-nanodegree-program-virtual-machine)
