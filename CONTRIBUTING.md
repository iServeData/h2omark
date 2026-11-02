# Contributing

Thanks for helping. h2omark adds a text watermark to an image.

## Get it running

Clone the repository (the **Code** button on GitHub), then from its folder:

```sh
python3 -m venv .venv
.venv/bin/pip install pillow
.venv/bin/python h2omark.py <image> "<watermark text>"
```

The result is saved next to the original as `<name>_h2o.<ext>`. Use your own test images and keep them
out of commits.

## Making a change

- Branch from `prototype` and open the pull request against `prototype`; `main` is what gets installed.
- Never commit real tokens, passwords, keys, IP addresses, Discord IDs, domains, or community, guild,
  channel, server or player names. Use placeholders such as `Example Community`,
  `community.example.org`, `203.0.113.10` and `000000000000000000`.
  CI runs `tools/check_generic.py`, which fails on addresses, IDs and private terms.
- Lowercase filenames with underscores, no spaces.
- Add a line to `CHANGELOG.md` describing the change.

## Security problems

Please don't open a public issue; see [SECURITY.md](SECURITY.md).
