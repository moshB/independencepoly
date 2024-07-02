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

def main1():
    # [65, 262, 447, 420, 235, 78, 14, 1]
    # gg = {0: [1, 2, 3, 4, 5, 6, 7, ], 1: [0, 8], 2: [0, 9], 3: [0, 10], 4: [0, 11], 5: [0, 12], 6: [0, 13], 7: [0],
    #       8: [1],
    #       9: [2], 10: [3], 11: [4], 12: [5], 13: [6]}
    m = 7
    g ={0:[]}
    for i in range(1,m):
        g[0].append(i)
        g[i]=[0,m+i]
        g[m+i]=[i]
    g[0].append(m)
    g[m]=[0]
    print(g)
    ip = get_independence_polynomial(g)
    print(ip)
    print(len(ip)-1)
    l = len(ip)
    maxi = 0
    for i in range(l):
        if ip[l-i-1]>maxi:
            maxi =ip[l-i-1]
        else:
            print(i-1)
            return




def main():
    l=110
    lenmin=0
    conn = sqlite3.connect('compactDB20.db')  # פתיחת חיבור לדטא-בייס. לשים לב שהדטא בייס נמצא באותה תיקיה
    with conn:  # שימוש ב DB שאוטומטית בסופו סוגר את החיבור
        cur = conn.cursor()  # יצירת מצביע ל DB
        cur.execute("SELECT * FROM trees WHERE Vertices = 9")  # בחירת כל הדטא שיש ל10 קודקודים
        rows = cur.fetchall()  # להכניס את כל הרשומות מהDB לתוך rows



        for row in rows:  # הדפסת כל הרשומות שנקראו מה DB
            # print(str(row))(14,7)(15,8)(16,9) (17,9), (18,9),(19,11) (20,10.11)(
            n=10
            g=convert_text_to_dict(row[0])
            ip=get_independence_polynomial(g)
            alfa = len(ip)-1
            pu=math.ceil((2*alfa-1)/3)
            pd = math.floor((alfa+1)/2)
            maxim = ip[0]
            maxend = ip[len(ip)-1]

            # if len(ip)<lenmin
            #     # print(len(ip))
            #     lenmin=len(ip)
            b = True
            for i in range(alfa,0,-1):
                if ip[i]>=maxend:
                    maxend = ip[i]
                elif b :#and (len(ip)-i)/(len(ip)-1)>0.6:
                    print((len(ip)-2-i)/(len(ip)-1))
                    if l>(len(ip)-i)/(len(ip)-1):
                        l=(len(ip)-i)/(len(ip)-1)
                    print(len(ip)-1)
                    print(ip)
                    print(g)
                    b = False
                    # if len(ip) < lenmin:
                    #     print(len(ip))
                    #     lenmin = len(ip)

                    if (len(ip)-2-i)/(len(ip)-1)<0.5:
                        print('so bad')
                        # return
    print("______________")
    print(l)
    print('lenmin-1')
    print(lenmin)




    print("DONE!")

if __name__ == '__main__':
    main1()