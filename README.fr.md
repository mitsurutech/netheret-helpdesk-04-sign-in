# Centre d'assistance Netheret, étape 04 : connexion

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un exemple pour enseigner. En seize étapes, nous construisons une application web de centre d'assistance pour Netheret, une entreprise imaginaire qui s'occupe de l'informatique de petites entreprises. Cette étape permet de se connecter et de se déconnecter, et donne à chaque rôle son propre tableau de bord.

## Ce que cette étape ajoute

- `helpdesk/auth.py` : les pages de connexion et de déconnexion, écrites à la main sans
  bibliothèque supplémentaire :
  - le mot de passe saisi est vérifié par rapport au hachage enregistré ;
  - l'id de l'utilisateur est gardé dans la `session` de Flask, un cookie signé avec la
    clé secrète ;
  - `load_signed_in_user` s'exécute avant chaque requête et définit `g.user` ;
  - `@login_required` et `@role_required(...)` protègent les pages.
- `SECRET_KEY` dans `helpdesk/__init__.py`, lue depuis une variable d'environnement.
- Un tableau de bord sur `/dashboard`, qui dit quelque chose de différent pour chaque rôle.
- Le menu change quand vous êtes connecté, avec un bouton Sign out.

## Lancer l'application

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Connectez-vous avec n'importe quel compte de démonstration, par exemple `manager@netheret.example`,
`tier1@netheret.example`, `tier2@netheret.example`, `tier3@netheret.example`
ou `customer@brightwell.example`. Le mot de passe de démonstration est le même pour tous :
`password123` (données d'exemple uniquement).

Sur un vrai serveur, vous définiriez d'abord une longue clé secrète aléatoire, par exemple
`export SECRET_KEY=...` sous macOS et Linux. Sans elle, l'application crée une nouvelle
clé aléatoire à chaque démarrage, et vous êtes donc déconnecté quand elle redémarre.

## À regarder

- Pourquoi le message d'erreur de connexion ne dit jamais quelle partie était fausse.
- `session.clear()` avant d'enregistrer l'id de l'utilisateur : une session neuve à chaque fois.
- La déconnexion est un formulaire envoyé en POST, pas un lien.
- Comment `role_required` est une fonction qui fabrique un décorateur.

## Apprendre cette étape

Voici l'étape 4 sur 16 de **Task 2. Developing the solution**, une série gratuite de leçons de T Level Digital Software Development, en anglais, qui construit le centre d'assistance Netheret en sprints agiles avec Python et Flask. Lisez la leçon de cette étape :
[Connexion, rôles et sessions](https://mitsurutech.co.uk/resources/t-level/dsd-t2-04-sign-in).

- Étape précédente : [étape 03, la base de données avec Flask-SQLAlchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- Étape suivante : [étape 05, créer une demande d'assistance](https://github.com/mitsurutech/netheret-helpdesk-05-raise-request)
- [Toutes les leçons gratuites de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseigner ces leçons à votre classe sur MitsuruTech](https://mitsurutech.co.uk/fr/learning), [voir les tarifs](https://mitsurutech.co.uk/fr/pricing) ou
  [commencer une année gratuite pour votre établissement](https://mitsurutech.co.uk/fr/signup)

## À propos

Écrit par [Mitsuru Technologies](https://mitsurutech.co.uk/fr) (MitsuruTech) comme exemple pédagogique pour le T Level Digital
Software Development. Le cahier des charges Netheret IT Support Solutions provient du matériel d'évaluation type de Pearson ; ce code
et ses notes sont les nôtres, et ne sont ni publiés, ni soutenus, ni approuvés par Pearson ou le Department for Education.
« T Level » est une marque déposée du Department for Education.
