# Dawid Mularczyk
from zad2testy import runtests

'''

nie chce mi sie robic opisu

'''

def snow( S ):
    def median(a, b, c):
        if b <= a <= c or c <= a <= b:
            return a
        elif a <= b <= c or c <= b <= a:
            return b
        elif a <= c <= b or b <= c <= a:
            return c

    def quicksort(T, p, r):
        if p < r:
            q = partition(T, p, r)
            quicksort(T, p, q)
            quicksort(T, q + 1, r)

    def partition(T, p, r):
        i = p - 1
        j = r + 1
        pivot = median(T[p], T[p + ((r - p) // 2)], T[r])
        while True:
            i += 1
            while T[i] > pivot:
                i += 1

            j -= 1
            while T[j] < pivot:
                j -= 1

            if i >= j: # sytuacja gdy lewy i prawy wskaznik sie spotka
                return j
            T[i], T[j] = T[j], T[i]

    n = len(S) - 1
    quicksort(S, 0, n)
    max_snow = 0
    for i in range(len(S)):
        if S[i] > i:
            max_snow += S[i] - i

    return max_snow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
