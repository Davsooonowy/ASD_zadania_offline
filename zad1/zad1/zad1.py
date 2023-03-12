# Dawid Mularczyk
from zad1testy import runtests

'''
Palindrom o nieparzystej długości ma na środku pojedyncza literkę. Wykorzystałem ten fakt i stworzyłem pętlę for
o ograniczonym przedziale(środek na pozycji 0 i n-1 da mi wynik 1, więc nie ma sensu go sprawdzać). W pętli for 
na początku sprawdzam czy pozycja po lewej i po prawej aktualnego środka jest taka sama, jeżeli tak to wykonuję pętlę 
while dopóki pozycja i - j == i + j [i to pozycja srodka, j jest zwiekszane o 1 w kazdej iteracji] oraz nie wyjdziemy
poza liste. Po przerwaniu petli while sprawdzam czy znaleziony palindrom jest najdłuższy. Po zakonczeniu petli for 
funkcja zwraca najwieksza dlugosc palindromu

Zlozonosc obliczeniowa podanego algorytmu w najgorszym przypadku wynosi O(N^2), w przypadku optymistycznym jest to O(N).

'''

def ceasar(s):
    n = len(s)
    curr_len, max_len = 1, 1

    if n == 0:
        return 0

    for i in range(1, n - 1):
        if s[i - 1] == s[i + 1]:
            j = 1
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                curr_len += 2
                j += 1
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1

    return max_len


runtests(ceasar, all_tests=True)