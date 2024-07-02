import networkx as nx

def canonical_form(G):
    """ Returns a canonical form (hashable) of the graph G """
    return nx.to_directed(nx.minimum_spanning_tree(G))

def generate_trees(n):
    """ Generates all non-isomorphic trees with n vertices """
    graphs = []

    def generate(current, remaining):
        if remaining == 0:
            canonical = canonical_form(current)
            if canonical not in graphs:
                graphs.append(canonical)
                yield current.copy()
            return
        for i in range(len(current)):
            current.add_edge(len(current), i)
            yield from generate(current, remaining - 1)
            current.remove_edge(len(current) - 1, i)

    if n == 1:
        yield nx.Graph()
    else:
        for tree in generate(nx.Graph(), n - 1):
            yield tree

def main():
    n = 5#int(input("Enter the number of vertices (n): "))
    print(f"All non-isomorphic trees with {n} vertices:")
    count = 0
    ts = generate_trees(n)
    print(len(ts))
    for tree in ts:
        count += 1
        print(f"Tree {count}: {tree.nodes()} vertices, {tree.edges()} edges")

if __name__ == "__main__":
    main()
