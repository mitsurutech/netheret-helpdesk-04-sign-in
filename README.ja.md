# Netheretヘルプデスク ステップ04：サインイン

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

授業のための作例です。16のステップで、小さな会社のITを支える架空の会社Netheretのために、ヘルプデスクのWebアプリを作っていきます。 このステップでは、サインインとサインアウトができるようにし、役割ごとにダッシュボードを用意します。

## このステップで加わるもの

- `helpdesk/auth.py`：サインインとサインアウトのページ。追加のライブラリを使わず、
  手で書いています。
  - 入力されたパスワードを、保存されたハッシュと照らし合わせます。
  - ユーザーのidを、秘密鍵で署名したクッキーであるFlaskの `session` に
    保存します。
  - `load_signed_in_user` がリクエストのたびに先に実行され、`g.user` を設定します。
  - `@login_required` と `@role_required(...)` がページを守ります。
- `helpdesk/__init__.py` の `SECRET_KEY`。環境変数から読み込みます。
- `/dashboard` のダッシュボード。役割ごとに違う内容を表示します。
- サインインするとメニューが変わり、Sign outボタンが出ます。

## 動かしてみる

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

どのデモ用アカウントでもサインインできます。たとえば `manager@netheret.example`、
`tier1@netheret.example`、`tier2@netheret.example`、`tier3@netheret.example`、
`customer@brightwell.example` です。デモ用パスワードはどれも
`password123` です（サンプルデータ専用）。

本番のサーバーでは、まず長くてランダムな秘密鍵を設定します。たとえばmacOSやLinuxでは
`export SECRET_KEY=...` です。設定しないと、アプリは起動のたびに新しいランダムな鍵を作るので、
再起動するとサインアウトされます。

## 注目するところ

- サインインのエラーが、どこが間違っていたかを決して言わない理由。
- ユーザーのidを保存する前の `session.clear()`：毎回まっさらなセッションにします。
- サインアウトはリンクではなく、POSTするフォームです。
- `role_required` が、デコレーターを作る関数になっているしくみ。

## このステップを学ぶ

これは **Task 2. Developing the solution** の16ステップ中のステップ4です。T Level Digital Software Developmentの無料レッスン（英語）のシリーズで、PythonとFlaskを使い、アジャイルのスプリントでNetheretのヘルプデスクを作ります。このステップのレッスンはこちらです：
[サインイン、役割、セッション](https://mitsurutech.co.uk/resources/t-level/dsd-t2-04-sign-in)。

- 前のステップ：[ステップ03「Flask-SQLAlchemyによるデータベース」](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- 次のステップ：[ステップ05「サポート依頼の登録」](https://github.com/mitsurutech/netheret-helpdesk-05-raise-request)
- [T Level Digitalの無料レッスン一覧](https://mitsurutech.co.uk/resources/t-level)
- [これらのレッスンをMitsuruTechでクラスに教える](https://mitsurutech.co.uk/ja/learning)、[料金を見る](https://mitsurutech.co.uk/ja/pricing)、
  [学校で無料の1年を始める](https://mitsurutech.co.uk/ja/signup)

## この作例について

T Level Digital Software Developmentの授業のための作例として、[Mitsuru Technologies](https://mitsurutech.co.uk/ja)（MitsuruTech）が書きました。
Netheret IT Support Solutionsの課題文はPearsonのサンプル評価資料によるものです。このコードと解説は私たち自身のもので、
PearsonやDepartment for Educationが公開、推奨、承認したものではありません。
「T Level」はDepartment for Educationの登録商標です。
