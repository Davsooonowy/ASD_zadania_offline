# Dawid Mularczyk
from zad5testy import runtests
from queue import PriorityQueue
'''
Algorytm na początku dodaje łączenia z jednej osobliwości do reszty(jest to wystarczająca ilość dodanych krawędzi, ponieważ
nie ma znaczenia ile razy przejdziemy po krawędziach osobliwości, czas podróży i tak będzie zerowy). Następnie zmieniam 
formę grafu na listę sąsiedztwa w postaci [[(v,w),...],...] następnie używam algorytmu dijkstry wzorowanego na wykładzie
w celu znalezienia najkrótszej ścieżki w grafie ważonym. Złożoność obliczeniową algorytmu oceniam na O(ElogV) gdzie E to
ilosc krawedzi w nowym grafie, natomiast V to ilosc planet'''


def relax(v, u, w, distances, parent, Q):
    if distances[v] > distances[u] + w:
        distances[v] = distances[u] + w
        parent[v] = u
        Q.put((distances[v], v))


def dijkstra(G, start, stop, n):
    distances = [float('inf')] * n
    distances[start] = 0
    parent = [None] * n
    Q = PriorityQueue()
    Q.put((0, start))

    while not Q.empty():
        (distance, current) = Q.get()

        if current == stop:
            break

        for (v, w) in G[current]:
            relax(v, current, w, distances, parent, Q)

    return distances[stop] if parent[stop] is not None else None


def spacetravel(n, E, S, a, b):
    for i in range(1, len(S)):
        E.append((S[0], S[i], 0))

    graph = [[] for _ in range(n)]

    for i in range(len(E)):
        graph[E[i][0]].append((E[i][1], E[i][2]))
        graph[E[i][1]].append((E[i][0], E[i][2]))

    return dijkstra(graph, a, b, n)


runtests(spacetravel, all_tests = True)