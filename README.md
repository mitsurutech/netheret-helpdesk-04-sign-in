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

<!-- links -->
