# Mastermind Game - Python

Mastermind to popularna gra logiczna, w której gracz lub komputer próbuje odgadnąć ukrytą sekwencję liczb. Ten projekt implementuje dwa tryby rozgrywki:
- AI Gameplay: komputer zgaduje ukrytą sekwencję, wykorzystując algorytm minimax.
- Player Gameplay: gracz zgaduje ukrytą sekwencję, podaną losowo przez program.

Algorytm minimax zaimplementowany w kodzie został stworzony na bazie angielskiej Wikipedii gry Mastermind.

## Struktura projektu

Projekt składa się z czterech głównych plików:

### 1. main.py
Główne wejście do programu. Obsługuje wybór trybu rozgrywki:
- Tryb AI (komputer zgaduje sekwencję).
- Tryb gracza (gracz zgaduje sekwencję).

### 2. ai_gameplay.py
Moduł obsługujący rozgrywkę w trybie, w którym komputer zgaduje ukrytą sekwencję.

Główne funkcje:
- Generowanie pierwszego zgadywania.
- Sprawdzanie poprawności zgadywań.
- Algorytm minimax do wyboru najlepszego ruchu.

### 3. player_gameplay.py
Moduł obsługujący tryb, w którym gracz zgaduje ukrytą sekwencję.

Główne funkcje:
- Generowanie ukrytej sekwencji.
- Zgadywanie sekwencji przez gracza.

### 4. judge.py
Moduł obsługujący mechanizm sprawdzania poprawności zgadywania.

Główna funkcja:
- Porównanie ukrytej sekwencji z zgadywaną.

## Jak uruchomić projekt?

1. Wymagania wstępne:
   - Python 3.9 lub nowszy.

2. Uruchomienie gry:
   - W terminalu (bash) wpisz:
     cd Mastermind
     python3 main.py
     
   - Wybierz tryb gry:
     - 1: Tryb AI Gameplay (komputer zgaduje sekwencję).
     - 2: Tryb Player Gameplay (gracz zgaduje sekwencję).
