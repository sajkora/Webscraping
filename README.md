# Aplikacja Webscrapingowa
## Aplikacja Webscrapingowa dla strony CoinGecko
## Aplikacja webscrapingowa jest narzędziem, które automatycznie pobiera dane z wybranej strony internetowej
## Jej główne cele i funkcje to:
- Pobieranie danych: Aplikacja pobiera informacje z witryny CoinGecko. Dane te obejmują między innymi:Ceny kryptowalut, wzrost lub spadek cen, podaż
- Wyświetlanie danych: Aplikacja wyświetla dane które pobrała w postaci tabeli
- Logowanie oraz Rejestracja: Użytkownicy po założeniu konta mogą dodawać wybrane kryptowaluty do ulubionych

| Identyfikator | Nazwa | Opis | Priorytet | Kategoria |
| ------------- | ----- | ---- | --------- | --------- |
| 1             | Scrapowanie giełdy kryptowalut | Aplikacja będzie scrapować dane ze strony o tematyce kryptowalut Coingecko | 1 | Wymagania funkcjonalne |
| 2             | Osadzenie w frameworku Flask   | Aplikacja będzie osadzona w webowym frameworku Flask w celu przedstawienia zescrapowanych danych | 1 | Wymagania funkcjonalne |
| 3             | Dostęp do arkusza całego z poziomu aplikacji     | Dostęp do całego zescrapowanego arkusza na stronie | 3 | Wymagania funkcjonalne |
| 4             | Mozliwosc pobrania arkusza     | Możliwość pobrania zescrapowanego arkusza za pomocą dedykowanego przycisku | 2 | Wymagania funkcjonalne |
| 5             | Dokumentacja     | Poświadczenie ze strony o legalności wykonywanego scrapingu | 2 | Wymagania funkcjonalne |




### Stos technologiczny
### Architektura rozwoju:
- Frontend: Flask, HTML, CSS
- Backend: Python

### Architektura uruchumieniowa:
- Python, Poetry

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
