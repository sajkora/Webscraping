# Instalacja Pythona i Poetry

## Zainstaluj pyenv: 

  WYWOLAJ TA KOMENDE W POWERSHELL (CALA): 
  `Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"`

  Dodaj C:\Users<nazwa_użytkownika>.pyenv do zmiennej PATH

## Zainstaluj Pythona 3.12.1:

  Uruchom `pyenv install 3.12.1` w PowerShellu

## Zainstaluj Poetry:

  Upewnij się, że masz Pythona 3.6+ 
  Uruchom `pip install poetry` w VSC/PyCharmie

## Ustaw in-project venv w Poetry:
  Otwórz folder projektu Uruchom `poetry init` w folderze projektu
  W pyproject.toml dodaj: tool.poetry.virtualenvs = in-project

## Wykonaj poetry install i shell:
  Uruchom poetry install w folderze projektu (w terminalu)
  Uruchom poetry shell w folderze projektu (w terminalu)

## Playwright:
  w shellu uruchom `playwright install`

