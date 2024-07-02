from itertools import combinations
from math import comb

import numpy as numpy


def count_isomorphisms(graph):
  """
  סופר את מספר העצים האיזומורפיים לגרף נתון.

  Args:
    graph: מילון המייצג את הגרף.

  Returns:
    מספר העצים האיזומורפיים.
  """
  nodes = list(graph.keys())
  visited = [False] * len(nodes)
  count = 0

  def dfs(i, parent):
    nonlocal count

    visited[i] = True
    for neighbor in graph[i]:
      if not visited[neighbor]:
        dfs(neighbor, i)
      elif neighbor != parent:
        count += 1

  for i in nodes:
    if not visited[i]:
      dfs(i, None)

  return count

def generate_trees(n):
  """
  מייצר את כל העצים הלא-איזומורפיים בעלי n קודקודים.

  Args:
    n: מספר הקודקודים בעץ.

  Returns:
    רשימה של מילונים המייצגים את העצים.
  """
  if n == 0:
    return []

  if n == 1:
    return [{0: []}]

  trees = []
  for i in range(1, n):
    subtrees = generate_trees(n - i - 1)
    for subtree in subtrees:
      graph = {j: [] for j in range(n)}
      for node in subtree:
        for neighbor in subtree[node]:
          graph[node + i].append(neighbor + i)

      # הוסף קשתות מהשורש לכל קודקוד בעץ המשנה
      for node in subtree:
        graph[0].append(node + i)
        graph[node + i].append(0)

      # סנן עצים איזומורפיים
      if True:#count_isomorphisms(graph) == 1:
        trees.append(graph)

  return trees

def characteristic_polynomial(graph):
  """
  מחשב את הפולינום האופייני של גרף נתון.

  Args:
    graph: מילון המייצג את הגרף.

  Returns:
    הפולינום האופייני כמחרוזת.
  """
  n = len(graph)
  adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
  for i in graph:
    for neighbor in graph[i]:
      adj_matrix[i][neighbor] = 1

  det = numpy.linalg.det(adj_matrix)
  poly = numpy.poly1d(det)
  return str(poly)

# הדגמה
n =1
trees = generate_trees(n)
for tree in trees:
  print("עץ:")
  print(tree)
  print("פולינום עצמי:")
  print(characteristic_polynomial(tree))




# הדגמה
# n = 4
# trees = generate_trees(n)
# print(len(trees))
# # print(trees)
# for tree in trees:
#   print(tree)

n=4
k=2
combinations_list = combinations(range(n), k)  # Creates an iterator
print(combinations_list)
num_combinations = sum(1 for _ in combinations_list)  # Count the number of elements in the iterator
print(comb(4, 2))