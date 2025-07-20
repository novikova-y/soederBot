# SöderDaily 🇩🇪✨

Nothing fascinates me as much as memes.  
After moving to Germany, I found myself discovering the local culture through humor — and naturally, that led me to Markus Söder.

This simple Telegram bot sends out a random Söder quote or gif on command. Built just for fun, to celebrate *Stabilität* and the unique charm of Bavarian politics.

👀 Try it here: [@SoederMaggus_bot](https://t.me/SoederMaggus_bot)

## Features

- `/start` — greets the user
- `/help` — returns a short instruction
- `/quote` — returns a random Markus Söder quote
- `/gif` — returns a random Markus Söder gif

## Tech stack

- Python 3  
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
- Token stored securely via environment variables (`.env` + `python-dotenv`)  
- Hosted on [Render](https://render.com/) with `webhook` support  

## To-do

- [ ] Add quote parser from online news  
- [x] Add funny Söder gifs  
- [x] Deploy to the cloud (done via Render ✅)

## Tests

- Currently, tests are included (but without CI/CD setup for the moment).

---

✨ Just a small side project to practice and share some *bayerischer Humor*.