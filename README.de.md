# Netheret-Helpdesk, Schritt 04: Anmeldung

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Ein Beispiel für den Unterricht. In sechzehn Schritten bauen wir eine Helpdesk-Webanwendung für Netheret, ein erfundenes Unternehmen, das die IT kleiner Firmen betreut. Dieser Schritt ermöglicht das An- und Abmelden und gibt jeder Rolle ihr eigenes Dashboard.

## Was dieser Schritt hinzufügt

- `helpdesk/auth.py`: die Seiten zum An- und Abmelden, von Hand geschrieben, ohne
  zusätzliche Bibliothek:
  - das eingegebene Passwort wird mit dem gespeicherten Hash verglichen;
  - die ID des Benutzers wird in der `session` von Flask gespeichert, einem Cookie, das mit dem
    geheimen Schlüssel signiert ist;
  - `load_signed_in_user` läuft vor jeder Anfrage und setzt `g.user`;
  - `@login_required` und `@role_required(...)` schützen Seiten.
- `SECRET_KEY` in `helpdesk/__init__.py`, aus einer Umgebungsvariablen gelesen.
- Ein Dashboard unter `/dashboard`, das für jede Rolle etwas anderes anzeigt.
- Das Menü ändert sich, wenn Sie angemeldet sind, mit einer Schaltfläche Sign out.

## Starten

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Melden Sie sich mit einem beliebigen Demo-Konto an, zum Beispiel `manager@netheret.example`,
`tier1@netheret.example`, `tier2@netheret.example`, `tier3@netheret.example`
oder `customer@brightwell.example`. Das Demo-Passwort ist für alle
`password123` (nur Beispieldaten).

Auf einem echten Server würden Sie zuerst einen langen, zufälligen geheimen Schlüssel setzen, zum Beispiel
mit `export SECRET_KEY=...` unter macOS und Linux. Ohne ihn erzeugt die Anwendung bei jedem Start einen neuen
zufälligen Schlüssel, sodass Sie nach einem Neustart abgemeldet sind.

## Worauf Sie achten sollten

- Warum die Fehlermeldung bei der Anmeldung nie sagt, welcher Teil falsch war.
- `session.clear()` vor dem Speichern der Benutzer-ID: jedes Mal eine frische Sitzung.
- Abmelden ist ein Formular, das per POST sendet, kein Link.
- Wie `role_required` eine Funktion ist, die einen Decorator erzeugt.

## Diesen Schritt lernen

Dies ist Schritt 4 von 16 aus **Task 2. Developing the solution**, einer kostenlosen Reihe von Lektionen zu T Level Digital Software Development auf Englisch, die den Helpdesk von Netheret in agilen Sprints mit Python und Flask baut. Lesen Sie die Lektion zu diesem Schritt:
[Anmeldung, Rollen und Sitzungen](https://mitsurutech.co.uk/resources/t-level/dsd-t2-04-sign-in).

- Vorheriger Schritt: [Schritt 03, Die Datenbank mit Flask-SQLAlchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- Nächster Schritt: [Schritt 05, Eine Supportanfrage stellen](https://github.com/mitsurutech/netheret-helpdesk-05-raise-request)
- [Alle kostenlosen Lektionen zu T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Diese Lektionen mit Ihrer Klasse auf MitsuruTech unterrichten](https://mitsurutech.co.uk/de/learning), [die Preise ansehen](https://mitsurutech.co.uk/de/pricing) oder
  [ein kostenloses Jahr für Ihre Schule beginnen](https://mitsurutech.co.uk/de/signup)

## Über dieses Beispiel

Geschrieben von [Mitsuru Technologies](https://mitsurutech.co.uk/de) (MitsuruTech) als Unterrichtsbeispiel für T Level Digital
Software Development. Die Aufgabenstellung Netheret IT Support Solutions stammt aus dem Muster-Prüfungsmaterial von Pearson; dieser Code
und seine Erläuterungen sind unsere eigenen und werden weder von Pearson noch vom Department for Education veröffentlicht, unterstützt oder genehmigt.
„T Level“ ist eine eingetragene Marke des Department for Education.
