import csv
fiels_name = ["Name", "Author", "Publisher", "Price", "Category"]
book1 = ["computer programming part1","Tamim Shariar Subeen","Onnorokom Prokashoni","240.00","programming"]
book2 = ["computer programming part2","Tamim Shariar Subeen","Dimik Prokashoni","250.00","programming"]
book3 = ["Learn programming with python","Tamim Shariar Subeen","Dimik Prokashoni","200.00","programming"]
book_list = [book1,book2,book3]

with open("book.csv","w") as csvf:
    book_writer = csv.writer(csvf,delimiter=",",quotechar = "\"",quoting=csv.QUOTE_MINIMAL)
    book_writer.writerow(fiels_name)
    for book in book_list:
        book_writer.writerow(book)