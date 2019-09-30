# Analytics Report Generator
This is prototype for a internal reporting tool, Report Generator, for a newspaper site. This tool will connect to a database, use SQL queries to analyze the log data, and print out the answers to some questions.

There are four files in this project:
- README.md: README file to get you started running this project
- report_generator.py: the report generator
- report_gen_helper.py: the report generator help function
- create_view.sql: the sql script to create view in the database
- report_example.txt: what you should get after running this project
## Getting Started
### Installation 
Install and configure the VM following the [instruction](https://github.com/udacity/fullstack-nanodegree-vm). 

### Get VM up and running
After navigating to the directory that the VM file are stored, run `vagrant up` and `vagrant ssh` to get the VM up and running. More detail see [Udacity Full Stack VM - start the virtual machine](https://github.com/udacity/fullstack-nanodegree-vm#start-the-virtual-machine)
If you have trouble with VM set up and running, refer to [Udacity Full Stack VM - troubleshooting](https://github.com/udacity/fullstack-nanodegree-vm#start-the-virtual-machine)

## Running the test
### Import News Database
- Download the [news database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), place it in the `/vagrant` directory
- Import the Database `news` using the following query.
```sh
psql -d news -f newsdata.sql
```

### Create view with postgresql
The create_view.sql file in this project includes the SQL script used for creating views in the `news` database. To run this file and create views in the database, run:
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

## Result
If the code ran successfully, you should be able to get the following result either in your terminal or in the result.txt file.
```
1. The most popular three articles of all time:
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views
2. The most popular article authors of all time: 
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
3. On which days did more than 1% of requests lead to errors
2016-07-17 - 2.26% errors
```

## Author
- Yuhuan Fan 

## Supporting Materials
- [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm#full-stack-web-developer-nanodegree-program-virtual-machine)

