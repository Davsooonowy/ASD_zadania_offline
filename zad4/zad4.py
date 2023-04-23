# Dawid Mularczyk
from zad4testy import runtests
from collections import deque

'''
algorytm w celu znalezienia najkrótszej ścieżki wykorzystuje bfs z wykładu z jedną modyfikacją(funkcja ta zwraca listę 
wierzchołków w znalezionej ścieżce). Jeżeli nie ma wymaganej ścieżki to funkcja zwraca None. Funkcja ,,longer'' na 
początku sprawdza czy istnieje taka ścieżka, jeżeli tak to w pętli iteruję po jej wierzchołkach. W każdej iteracji usuwam 
jedną krawędź i sprawdzam czy zmieniła się długość najkrótszej ścieżki, jeżeli tak to zwracam wierzchołki tej krawędzi. 
W przeciwnym wypadku przywracam krawędź do grafu. I w następnej iteracji biorę kolejną krawędź do sprawdzenia. Funkcja
Oceniam Złożoność obliczeniową podanego algorytmu na O(V*(V + E)),gdzie V to ilość wierzchołków a E to ilość krawędzi.
BFS ma złożoność O(V + E) i wywołuję te funkcję co najwyżej V - 1 razy (maksymalna dlugosc sciezki w grafie) w pętli for. 
'''


def bfs(G, s, t):
    n = len(G)
    visited = [False] * n
    visited[s] = True
    parent = [None] * n
    Q = deque()
    Q.append(s)
    while len(Q) != 0:
        u = Q.popleft()
        if u == t:
            path = []
            while u is not None:
                path.append(u)
                u = parent[u]
            return path

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.append(v)
    return None


def longer(G, s, t):
    path_exist = bfs(G, s, t)
    if path_exist is None:
        return None

    vertices = path_exist
    n = len(vertices)

    for i in range(1, len(vertices)):
        v1, v2 = vertices[i], vertices[i - 1]
        G[v1].remove(v2)
        G[v2].remove(v1)
        path_len = bfs(G, s, t)
        if path_len is None or len(path_len) > n:
            return (v1, v2)
        G[v1].append(v2)
        G[v2].append(v1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )