# The World Today — 20 November 2026 in one image

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/xulei524926-blip/world-news-one-image/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/xulei524926-blip/world-news-one-image/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

An entry for make.fun's **"Sum up 20 November's world news in one image"**
bounty. The whole day, set as a broadsheet front page:

- **Three rivals, one table** — Trump, Xi and Putin meet in Shenzhen for
  the first US–China–Russia summit in history and sign a joint peace
  declaration.
- **Myanmar guilty of genocide** — the World Court's first genocide
  ruling against a state, over the Rohingya.
- **AI debut soars, markets sink** — Anthropic's record-breaking Nasdaq
  debut while the S&P 500 falls for a fifth straight day.
- **Missile hits Riyadh tower** — a Houthi strike damages the PIF
  skyscraper.
- **Crimea Bridge struck again** — the third Ukrainian strike in four
  days.
- In the ticker: Kenya ends its Ebola outbreak after 37 days, GTA 6 tops
  $2.3B in launch sales, Voyager 1 phones home from one light-day away,
  the COP31 draft ditches the fossil-fuel phase-out, a Van Gogh sells
  for a record $190.4M, and Italy fines Meta €805M.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
committed front-page image `entry.png` to `/output/entry.png`, byte for
byte, so every run produces the identical image (1024×1024 PNG, under
1 MiB).

The five illustrations were generated as a matching set in a flat
editorial style; every headline and caption was typeset programmatically
so the text stays crisp and legible — the image has to speak for itself,
because the judge sees only the picture.

## Run it

```sh
python3 main.py   # writes /output/entry.png
```
