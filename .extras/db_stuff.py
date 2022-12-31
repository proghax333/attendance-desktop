

# Create the connection
# con = QSqlDatabase.addDatabase("QSQLITE")
# con.setDatabaseName("contacts.sqlite")

# # Open the connection
# if not con.open():
#     print("Database Error: %s" % con.lastError().databaseText())
#     sys.exit(1)


# # Create a query and execute it right away using .exec()
# createTableQuery = QSqlQuery()
# createTableQuery.exec(
#     """
#     CREATE TABLE contacts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
#         name VARCHAR(40) NOT NULL,
#         job VARCHAR(50),
#         email VARCHAR(40) NOT NULL
#     )
#     """
# )

# print(con.tables())

# values = "('Ok', 'thing', 'ok')"
# for i in range (1, 100000):
#   values += f", ('{i}', 'okok thing {i}', 'thing {i ** 2}')"

# query = QSqlQuery()
# query.prepare(f'''
#   insert into contacts (name, job, email)
#   values {values}
# ''')
# query.bindValue(":id", i)
# query.bindValue(":name", "Shae " + str(i))
# query.bindValue(":email", "Hatter" + str(i ** 2))

# query.exec()


con = sqlite3.connect("contacts.db")
# cur = con.cursor()

# print("Started")
# cur.execute("select * from contacts where email like 'thing %'")
# data = cur.fetchall()
# print("Done!")
# print(len(data))
