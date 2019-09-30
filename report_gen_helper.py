#!/usr/bin/python3
import psycopg2

def report_gen(query, question):
    '''
    Generate a analysis report.

    query: the SQL query for the aggregation to generate the report.
    question: question that query answers and make the report readable.
    '''

    # connect to db and create cursor
    conn = psycopg2.connect(dbname="news")
    cursor = conn.cursor()

    # run query
    cursor.execute(query)
    results = cursor.fetchall()

    # print out report
    print(question)

    for res in results:
        if res[1] < 1:
            print("{} - {:.2%} errors".format(res[0], res[1]))
        else:
            print("{} - {} views".format(res[0], str(res[1])))
    conn.close()
