from report_gen_helper import report_gen

# def variables
question_list = [
    "1. The most popular three articles of all time:",
    "2. The most popular article authors of all time: ",
    "3. On which days did more than 1% of requests lead to errors"]

query_list = [
    "select articles.title, count(*) as views\
    from articles, log\
    where log.path like concat('%', articles.slug)\
    group by articles.title \
    order by views desc\
    limit 3;",
    "select authors.name, count(*) as views\
    from authors, articles, log\
    where articles.author = authors.id\
    and log.path like concat('%', articles.slug)\
    group by authors.name\
    order by views desc;",
    "select * from error_rate_table\
    where error_rate > 0.01;"
]


for i in list(range(3)):
    report_gen(query_list[i], question_list[i])
