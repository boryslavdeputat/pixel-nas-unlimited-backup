# Pixel NAS Unlimited Backup

**Languages:** [English](README.md) · [Українська](README.uk.md)

> Practical reference by [Boryslav Deputat](https://github.com/boryslavdeputat) - Cloud / SRE / Platform.
> Sites: [Portfolio](https://boryslavdeputat.com/) · [ClawDBot / KLAV (UA AI)](https://clawdbot.llc/) · [Walk ATX Pet](https://walkatxpet.com/) · [DepuTater](https://deputater.com/)

Unlimited media backup pipeline: **SMB/NAS -> rooted Pixel (Magisk module) -> Google Photos Original quality** with free-space safety, done-list, and buffer control.

## Why

Phones with small internal storage cannot hold multi-TB photo libraries. This design uses a spare rooted Pixel as a **gateway device**: pull from NAS with rclone, let Google Photos upload Original, then free space safely.

## Components

| Piece | Role |
|-------|------|
| Magisk module | Boot service + manual action |
| rclone | Copy from SMB/NAS (not fragile FUSE mounts) |
| buffer / hold dirs | Stage files without filling disk |
| `done.list` | Avoid re-copy of already processed media |
| free-space floor | Stop before device bricks itself |

## Safety rules

1. Never fill disk - enforce free-space floor (e.g. multi-GB free)
2. Prefer copy pipeline over CIFS kernel mounts when `cifs.ko` missing
3. Delete local only after Photos has a chance to upload (hold window)
4. Track completed remote paths in `done.list`

## Layout (typical module)

```
module/
  service.sh      # boot loop
  action.sh       # manual Magisk action
  util_common.sh
  config.example
```

## Docs

- `docs/ARCHITECTURE.md`
- `docs/SETUP.md`
- `docs/TUNING.md`
- `docs/TROUBLESHOOTING.md`

## Related

Built with **KLAV (UA AI) / КЛАВ (УКР ШІ)**. Portfolio: https://boryslavdeputat.com/

## Disclaimer

Educational and practical reference. Validate against your compliance, cost, and SLO requirements before production use.

## Contact

- Portfolio: https://boryslavdeputat.com/
- ClawDBot / KLAV (UA AI): https://clawdbot.llc/
- Email: info@boryslavdeputat.com

## License

MIT - see [LICENSE](LICENSE).
