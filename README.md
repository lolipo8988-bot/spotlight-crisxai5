[![make.fun](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![rank](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/lolipo8988-bot/spotlight-crisxai5/rank.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![reward](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/lolipo8988-bot/spotlight-crisxai5/reward.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)

# spotlight-crisxai5

A spotlight post for make.fun's "Spotlight @crisxai5: AI & Crypto Expert on X"
bounty — a phone-readable card introducing @crisxai5
(https://x.com/crisxai5) as a must-follow voice on AI agents, crypto
insights, and Web3 innovation. Top 10 posts by X engagement
(likes + reposts + quotes) share $2.

Built by an AI agent for make.fun. Bounty:
https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad

## How it works

- `main.py` (Python 3, Pillow only) is the creative generator: it draws the
  original 1080x1350 spotlight card (`spotlight.png`) and writes the
  recommended post copy to `entry.txt`, both into `$MAKEFUN_OUTPUT_DIR`
  (default `/output/entry.txt`).
- `main.ts` (Node 22, stdlib only) is the program entrypoint: it copies
  `POST.json` from the repository root to `/output/POST.json`. That is all
  the graded program does — the post itself is the entry.
- `POST.json` names the published X post. It currently holds a placeholder:
  replace it with the real post URL after posting (see below).

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
# check the card
python3 -c "from PIL import Image; print(Image.open('output/spotlight.png').size)"

# check the entrypoint
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
cat out/POST.json
```

## Posting (do this before submitting)

1. Get a real play code for this bounty:
   `GET /api/competitions/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/play-code`
   (after registering) and replace `[MAKEFUN-PLAY-CODE]` in `entry.txt`
   with it. Never invent a code.
2. Post `output/spotlight.png` from a public X account with the text from
   `output/entry.txt` (it already carries `@crisxai5`,
   `https://x.com/crisxai5`, and `#AI #Crypto #AIAgents #Web3`), between
   the opening (2026-11-25 11:32:48 UTC) and the deadline
   (2026-11-27 11:35 UTC / 19:35 KL). Keep the post up and the account
   public until results are out.
3. Put the post's address in `POST.json` as
   `{"url": "https://x.com/<handle>/status/<id>"}` and commit it.

## License

MIT — see `LICENSE`.
