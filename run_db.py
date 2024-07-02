import sqlite3

conn = sqlite3.connect('compactDB20.db')
cursor = conn.cursor()

# Get schema of a specific table (replace 'table_name' with actual name)
def get_schema(table_name):
    cursor.execute(f"PRAGMA table_info('{table_name}')")  # Using f-string for dynamic table name
    schema = cursor.fetchall()
    return schema

# Example usage:
table_name = 'trees'  # Replace with your table name
schema = get_schema(table_name)
# Table Schema:
#   - Column Name: Graph (Type: TEXT)
#   - Column Name: Vertices (Type: INTEGER)

# Print table schema
print("Table Schema:")
for row in schema:
    # print(row)
    print(f"  - Column Name: {row[1]} (Type: {row[2]})")

conn.close()

import sqlite3

def get_graph(table_name, id):
    conn = sqlite3.connect('compactDB20.db')
    cursor = conn.cursor()

    # Retrieve graph data for the specific record
    # cursor.execute(f"SELECT Graph FROM trees")
    cursor.execute("SELECT * FROM trees LIMIT 1 OFFSET 1346023")
    graph_data = cursor.fetchone()#[5]
    print(graph_data)
    print()

    # Parse the graph data (assuming adjacency list format)
    # graph = {}
    # for line in graph_data.split('\n'):
    #     node, neighbors = line.split(':')
    #     graph[node] = [int(neighbor) for neighbor in neighbors.split()]

g=get_graph('trees','graphs')
# print(g)
# # Get table names
# # cursor.execute(".tables")
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# tables = cursor.fetchall()
# for table in tables:
#     print(table[0])  # Print table name trees
#
# # Get schema of a specific table (replace 'table_name' with actual name)
# cursor.execute(".schema table_name")
# schema = cursor.fetchall()
# for row in schema:
#     print(row[0], row[1])  # Print column name and data type
#
# # Get data from a table (replace 'table_name' with actual name)
# cursor.execute("SELECT * FROM table_name")
# data = cursor.fetchall()
# for row in data:
#     print(row)  # Print each row of data
#
# conn.close()
