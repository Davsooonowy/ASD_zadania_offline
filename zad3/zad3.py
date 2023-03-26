# Dawid Mularczyk
from zad3testy import runtests

'''
mój algorytm wykorzystuje sortowanie merge_sort. Jest to standardowa implementacja merge_sort z jedną zmianą. Mianowicie
wykorzystuje funkcje compare, której używam do porównania dwóch napisów. Umożliwia mi ona uporządkowanie wyrazów równoważnych
obok siebie. Zanim używam funkcji merge sort używam list comprehension, w celu zamienienia każdego elementu w liście na 
ten element oraz jego odwrotność. Następnie iteruję po posortowanej liście krotek i szukam najdłuższego ciągu wyrazów
równoważnych. Złożoność obliczeniową algorytmu oceniam na O(NlogN + N).
'''


def strong_string(T):
    def merge_sort(T):
        def compare(s1, s2):
            # funkcja compare porownujaca minimum z napisu 1 i napisu 2
            return min(s1[0], s1[1]) <= min(s2[0], s2[1])

        if len(T) <= 1:
            return T

        # podzielenie tablicy na 2 części
        mid = len(T) // 2
        left = T[:mid]
        right = T[mid:]

        # wywołanie rekurencyjne
        merge_sort(left)
        merge_sort(right)

        # merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                T[k] = left[i]
                i += 1
            else:
                T[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            T[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            T[k] = right[j]
            j += 1
            k += 1

    T = [(T[i], T[i][::-1]) for i in range(len(T))]
    merge_sort(T)
    n = len(T)
    curr_max_len, max_len, i = 1, 1, 1
    while i < n:
        while i < n and (T[i][0] == T[i - 1][0] or T[i][0] == T[i - 1][1]):
            curr_max_len += 1
            i += 1
        if curr_max_len > max_len:
            max_len = curr_max_len
        curr_max_len = 1
        i += 1
    return max_len


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
# Dawid Mularczyk
from zad3testy import runtests
