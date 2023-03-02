
from pypika import Tables

def query(connection, query):
  cursor = connection.cursor()
  result = cursor.execute(query)
  rows = result.fetchall()
  columns = [description[0] for description in cursor.description]

  return {
    "cursor": cursor,
    "result": result,
    "rows": rows,
    "count": len(rows),
    "columns": columns,
    "connection": connection,
    "query": query
  }

devices, members, contacts = Tables("devices", "members", "contacts")
