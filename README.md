# Aplikacja Webscrapingowa
## Aplikacja Webscrapingowa dla strony CoinGecko
## Aplikacja webscrapingowa jest narzędziem, które automatycznie pobiera dane z wybranej strony internetowej
## Jej główne cele i funkcje to:
- Pobieranie danych: Aplikacja pobiera informacje z witryny CoinGecko. Dane te obejmują między innymi: Ceny kryptowalut, wzrost lub spadek cen, podaż
- Wyświetlanie danych: Aplikacja wyświetla dane które pobrała w postaci tabeli
- Logowanie oraz Rejestracja: Użytkownicy po założeniu konta mogą dodawać wybrane kryptowaluty do ulubionych
- Dodawanie oraz usuwanie kryptowalut do ulubionych, które można wyświetlić w zakładce Profil
- Możliwość pobrania zescrapowanego arkusza 

| Identyfikator | Nazwa | Opis | Priorytet | Kategoria |
| ------------- | ----- | ---- | --------- | --------- |
| 1             | Scrapowanie giełdy kryptowalut | Aplikacja będzie scrapować dane ze strony o tematyce kryptowalut Coingecko | 1 | Wymagania funkcjonalne |
| 2             | Osadzenie w frameworku Flask   | Aplikacja będzie osadzona w webowym frameworku Flask w celu przedstawienia zescrapowanych danych | 1 | Wymagania funkcjonalne |
| 3             | Dostęp do arkusza całego z poziomu aplikacji     | Dostęp do całego zescrapowanego arkusza na stronie | 1 | Wymagania funkcjonalne |
| 4             | Logowanie i rejestracja     | Użytkownicy aby korzystać z aplikacji muszą być zalogowani | 1 | Wymagania funkcjonalne |
| 5             | Dodawanie i usuwanie ulubionych kryptowalut     | Dostęp do listy ulubionych kryptowalut w zakładce Profil | 2 | Wymagania funkcjonalne |
| 6             | Mozliwosc pobrania arkusza     | Możliwość pobrania zescrapowanego arkusza za pomocą dedykowanego przycisku | 2 | Wymagania funkcjonalne |
| 7             | Dokumentacja     | Rozstrzygnięcie legalności wykonywanego scrapingu | 3 | Wymagania niefunkcjonalne |

## Autorzy
- Adrian Sikora
- Mikołaj Czarnecki
- Kacper Olszewski

## Licencja MIT

### ===========================================================

### Stos technologiczny
### Architektura rozwoju:
- Frontend: Flask, HTML, CSS
- Backend: Python, MySQL

### Wykorzystane biblioteki:
- BeautifulSoup - biblioteka umożliwiająca scraping danych poprzez przeglądanie kodu HTML wybranej strony
- Playwright - biblioteka imitująca przeglądarkę w celu ułatwienia scrapingu
- Pandas - biblioteka umożliwiająca manipulację danymi

### Architektura uruchomieniowa:
- Python - obsługa całej aplikacji
- Poetry - narzędzie do zarządzania zależnościami ułatwiające konfigurację projektu
- MySql - baza danych przechowująca zescrapowane dane


### ===========================================================
## Testy
- Scraping giełdy kryptowalut
  - Skrypt do scrapowania giełdy kryptowalut uruchamiany jest wraz z aplikacją.

- Autentykacja
  - Niezalogowany użytkownik powinien móc wyświetlić tylko i wyłącznie stronę startową.

- Rejestracja użytkowników
  - Użytkownik powinien mieć możliwość zarejestrowania się w aplikacji z poziomu strony startowej.

- Logowanie użytkowników
  - Użytkownik powinien mieć możliwość zalogowania się w aplikacji z poziomu strony startowej.

- Losowanie kryptowalut
  - Zalogowany użytkownik powinien mieć możliwość wylosowania jednej z kilkuset dostępnych kryptowalut.

- Dostęp do całego arkusza
  - Zalogowany użytkownik powinien mieć możliwość przejrzenia wszystkich zescrapowanych danych.

- Pobranie arkusza
  - Zalogowany użytkownik powinien mieć możliwość pobrania wszystkich zescrapowanych danych.

- Dodanie kryptowalut do sekcji ulubione w ramach śledzenia ich zmian
  - Zalogowany użytkownik powinien mieć możliwość dodania wielu kryptowalut do sekcji "ulubione" z poziomu tabeli ze wszystkimi kryptowalutami. Jedną kryptowalutę mógłby dodać tylko raz.

- Usuwanie kryptowalut z sekcji ulubione
  - Zalogowany użytkownik powinien mieć możliwość usunięcia kryptowalut z sekcji "ulubione" ze swojego profilu.

- Wyszukiwanie kryptowalut
  - Zalogowany użytkownik powinien mieć możliwość korzystania z pola wyszukiwania aby ułatwić dostęp do sprawdzenia konkretnej kryptowaluty. 
Biblioteki:


### ===========================================================
### Instalacja Pythona i Poetry
### Zainstaluj pyenv: 

  WYWOLAJ TA KOMENDE W POWERSHELL (CALA): 
  `Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"`

  Dodaj C:\Users<nazwa_użytkownika>.pyenv do zmiennej PATH

### Zainstaluj Pythona 3.12.1:

  Uruchom `pyenv install 3.12.1` w PowerShellu

### Zainstaluj Poetry:

  Upewnij się, że masz Pythona 3.6+
 
  Uruchom `pip install poetry` w VSC/PyCharmie

### Ustaw in-project venv w Poetry:
  Otwórz folder projektu
  
  Uruchom `poetry init` w folderze projektu
  
  Uruchom `Poetry config virtualenvs.in-project true` w terminalu

### Wykonaj poetry install i shell:
  Uruchom `poetry install` w folderze projektu (w terminalu)

  Uruchom `poetry shell` w folderze projektu (w terminalu)

### Playwright:
  w shellu uruchom `playwright install`
  w shellu `playwright install-deps`
