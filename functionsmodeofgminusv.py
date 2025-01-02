import json
import math
import sqlite3


#  פונקציה שממירה את הגרף שכתוב כטקסט בDB למילון שמייצג את הגרף כרשימת שכנויות
def convert_text_to_dict(adjacency_list):
    # Example:
    # "{0: [1, 2, 3, 4], 1: [0, 5, 6], 2: [0], 3: [0], 4: [0], 5: [1, 7], 6: [1], 7: [5, 8], 8: [7]}"
    # To:
    # {0: [1, 2, 3, 4], 1: [0, 5, 6], 2: [0], 3: [0], 4: [0], 5: [1, 7], 6: [1], 7: [5, 8], 8: [7]}

    s = adjacency_list.strip()

    graph = dict()
    s1 = s[1: -2].replace(" [", "").split("], ")
    for s2 in s1:
        s3 = s2.split(":")
        key = int(s3[0])
        values = s3[1].split(", ")
        values = list(map(int, values))
        graph[key] = values
    return graph


# פונקציה שמקבלת גרף כמילון של רשימת שכנויות ומחזירה רשימה של ה IP
def get_independence_polynomial(graph):
    graph_keys = list(graph.keys())
    global color, i_of_g_minus_v, i_of_g_minus_nv, i_of_g, hierarchy

    # initialize
    color = dict()
    i_of_g_minus_v = dict()
    i_of_g_minus_nv = dict()
    i_of_g = dict()
    hierarchy = dict()

    for key in graph:
        color[key] = 0
        i_of_g_minus_v[key] = []
        i_of_g_minus_nv[key] = []
        i_of_g[key] = []
        hierarchy[key] = []
    roots = []

    for i in graph_keys:
        if color[i] == 0:
            root = i
            roots.append(i)
            color[i] = 1
            _dfs_visit(graph, root)

    ans = [1]
    for r in roots:
        ans = polynomial_mul(ans, i_of_g[r])
    return ans


# פונקציית עזר ל get_independence_polynomial
def _dfs_visit(graph, root):
    # check if root has white neighbor. if not we reach a leaf or it isolated vertex
    has_white_neighbor = False
    for ne in graph[root]:
        if color[ne] == 0:
            has_white_neighbor = True
    if not has_white_neighbor:
        i_of_g_minus_v[root] = [1]
        i_of_g_minus_nv[root] = [1]
        i_of_g[root] = [1, 1]
        color[root] = 2

    else:
        for n_root in graph[root]:  # going to all root children (color == 0)
            if color[n_root] == 0:
                color[n_root] = 1
                hierarchy[root].append(n_root)  # set n_root ad child of root
                _dfs_visit(graph, n_root)

        left_mul = [1]
        right_mul = [1, 0]
        for n_root in hierarchy[root]:
            left_mul = polynomial_mul(left_mul, i_of_g[n_root])
            right_mul = polynomial_mul(right_mul, i_of_g_minus_v[n_root])

        i_of_g_minus_v[root] = left_mul
        i_of_g_minus_nv[root] = right_mul
        i_of_g[root] = polynomial_add(left_mul, right_mul)

        color[root] = 2


# כפל פולינומים
def polynomial_mul(p1, p2):
    """
    :param p1: [an, an-1, ..., a0] = a_nx^n+a_(n-1)x^(n-1)+...+a_1x+a_0
    """
    size_of_ans = len(p1) + len(p2) - 1
    ans = [0] * size_of_ans
    _p1 = p1[::-1]
    _p2 = p2[::-1]
    for i in range(len(_p1)):
        for j in range(len(_p2)):
            ans[i + j] += _p1[i] * _p2[j]
    return ans[::-1]


# חיבור פולינומים
def polynomial_add(p1, p2):
    size_of_ans = max(len(p1), len(p2))
    ans = [0] * size_of_ans
    _p1 = p1[:]
    _p2 = p2[:]
    _p1.reverse()
    _p2.reverse()

    if len(_p1) > len(_p2):
        diff = len(_p1) - len(_p2)
        _p2 += [0] * diff
    else:
        diff = len(_p2) - len(_p1)
        _p1 += [0] * diff

    for i in range(len(_p1)):
        ans[i] = _p1[i] + _p2[i]

    ans.reverse()
    return ans


from collections import deque


def is_unimodal(polynomial):
    """
    Check if a polynomial is unimodal.

    :param polynomial: List of coefficients of the polynomial.
    :return: True if the polynomial is unimodal.
    :raises ValueError: If the polynomial is not unimodal.
    """
    if not polynomial:
        raise ValueError("Polynomial is empty.")

    n = len(polynomial)
    if n == 1:
        return True

    # Check if the polynomial has increasing and then decreasing sequence
    peak_found = False
    for i in range(1, n):
        if polynomial[i] > polynomial[i - 1]:
            if peak_found:
                raise ValueError("Polynomial is not unimodal.")
        elif polynomial[i] < polynomial[i - 1]:
            peak_found = True

    return True


def bfs(graph, start):
    """Perform BFS and return the distances from the start node to all other nodes."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):  # Not visited
                queue.append(neighbor)
                distances[neighbor] = distances[current] + 1

    return distances


def graph_diameter(graph):
    """Return the diameter of the graph."""
    diameter = 0

    for node in graph:
        distances = bfs(graph, node)
        max_distance = max(distances.values())
        diameter = max(diameter, max_distance)

    return diameter


def remove_vertex(graph):
    graphs = []
    for vertex in graph:
        new_graph = {v: [n for n in neighbors if n != vertex] for v, neighbors in graph.items() if v != vertex}
        graphs.append(new_graph)
    return graphs


def calculate_mode(polynomial_coefficients):
    # Find the maximum coefficient and its index
    mode_index = -1 + len(polynomial_coefficients) - polynomial_coefficients.index(max(polynomial_coefficients))
    return mode_index


def main():
    conn = sqlite3.connect('compactDB20.db')  # פתיחת חיבור לדטא-בייס. לשים לב שהדטא בייס נמצא באותה תיקיה
    with conn:  # שימוש ב DB שאוטומטית בסופו סוגר את החיבור
        cur = conn.cursor()  # יצירת מצביע ל DB
        cur.execute("SELECT * FROM trees WHERE Vertices = 18")  # 7")  # בחירת כל הדטא שיש ל10 קודקודים17
        rows = cur.fetchall()  # להכניס את כל הרשומות מהDB לתוך rows

        for row in rows:  # הדפסת כל הרשומות שנקראו מה DB;
            graph = convert_text_to_dict(row[0])
            ip = get_independence_polynomial(graph)
            mode = calculate_mode(ip)

            graphs_without_vertices = remove_vertex(graph)
            for i, g in enumerate(graphs_without_vertices):
                ip_v = get_independence_polynomial(g)
                m = calculate_mode(ip_v)
                if m < mode - 1:
                    print('eror')


if __name__ == '__main__':
    main()
