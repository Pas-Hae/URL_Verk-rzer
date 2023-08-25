# URL-Verkürzer mit Bitly-API

Dieses Projekt enthält ein Python-Skript, das die Bitly-API verwendet, um lange URLs zu verkürzen. Der Benutzer kann einen langen URL eingeben, und das Skript generiert einen verkürzten URL, der dann in einer Textdatei gespeichert wird.

## Voraussetzungen

- Python 3.x
- `requests` Bibliothek
- Ein Bitly-API-Token

## Installation

1. Klone dieses Repository:

    ```bash
    git clone https://github.com/IhrGitHubBenutzername/URL-Verkuerzer.git
    ```

2. Wechseln Sie in das Verzeichnis des Projekts:

    ```bash
    cd URL-Verkuerzer
    ```

3. Installieren Sie die erforderlichen Pakete:

    ```bash
    pip install -r requirements.txt
    ```

## Verwendung

1. Fügen Sie Ihren Bitly-API-Token in das Skript ein:

    ```python
    api_token = "IHR_BITLY_API_TOKEN_HIER_EINFUEGEN"
    ```

2. Führen Sie das Skript aus:

    ```bash
    python url_verkuerzer.py
    ```

3. Geben Sie den langen URL ein, wenn Sie dazu aufgefordert werden.

4. Der verkürzte URL wird in der Konsole angezeigt und in der Datei `verkuerzte_links.txt` gespeichert.


