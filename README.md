# Netheret help desk, step 04: sign-in

A teaching example. Over sixteen steps we build a help desk web app for
Netheret, a made-up company that supports the IT of small businesses. This
step lets people sign in and out, and gives each role its own dashboard.

## What this step adds

- `helpdesk/auth.py`: the sign in and sign out pages, written by hand with
  no extra library:
  - the password typed in is checked against the stored hash;
  - the user's id is saved in Flask's `session`, a cookie signed with the
    secret key;
  - `load_signed_in_user` runs before every request and sets `g.user`;
  - `@login_required` and `@role_required(...)` protect pages.
- `SECRET_KEY` in `helpdesk/__init__.py`, read from an environment variable.
- A dashboard at `/dashboard` that says something different for each role.
- The menu changes when you are signed in, with a Sign out button.

## Run it

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Sign in with any demo account, for example `manager@netheret.example`,
`tier1@netheret.example`, `tier2@netheret.example`, `tier3@netheret.example`
or `customer@brightwell.example`. The demo password for all of them is
`password123` (sample data only).

On a real server you would set a long random secret key first, for example
`export SECRET_KEY=...` on macOS and Linux. Without one, the app makes a new
random key each time it starts, so you are signed out when it restarts.

## What to look at

- Why the sign in error never says which part was wrong.
- `session.clear()` before saving the user's id: a fresh session each time.
- Sign out is a form that POSTs, not a link.
- How `role_required` is a function that makes a decorator.

## Learn this step

This is step 4 of 16 of **Task 2. Developing the solution**, a free series of T Level Digital Software Development
lessons that builds the Netheret help desk in agile sprints with Python and Flask. Read the lesson for this step:
[Signing in, roles and sessions](https://mitsurutech.co.uk/resources/t-level/dsd-t2-04-sign-in).

- Previous step: [step 03, the database with flask-sqlalchemy](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- Next step: [step 05, raising a support request](https://github.com/mitsurutech/netheret-helpdesk-05-raise-request)
- [Every free T Level Digital lesson](https://mitsurutech.co.uk/resources/t-level)
- [Teach these lessons to your class on MitsuruTech](https://mitsurutech.co.uk/learning), [see the pricing](https://mitsurutech.co.uk/pricing) or
  [start a free year for your college](https://mitsurutech.co.uk/signup)

## About

Written by [Mitsuru Technologies](https://mitsurutech.co.uk) (MitsuruTech) as a teaching example for T Level Digital
Software Development. The Netheret IT Support Solutions brief is from Pearson's sample assessment material; this code
and its notes are our own, and are not published, endorsed or approved by Pearson or the Department for Education.
'T Level' is a registered trade mark of the Department for Education.

