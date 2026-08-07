# Pixel NAS Unlimited Backup

**Мови:** [English](README.md) · [Українська](README.uk.md)

> Практичний матеріал від [Boryslav Deputat](https://github.com/boryslavdeputat) - Cloud / SRE / Platform.
> Сайти: [Portfolio](https://boryslavdeputat.com/) · [ClawDBot / KLAV (UA AI)](https://clawdbot.llc/) · [Walk ATX Pet](https://walkatxpet.com/) · [DepuTater](https://deputater.com/)

Пайплайн бекапу медіа: NAS -> rooted Pixel -> Google Photos Original.

## Безпека

1. Не заповнювати диск - free-space floor
2. rclone copy замість крихких FUSE/CIFS mount, коли модулів ядра немає
3. Локальне видалення лише після hold-вікна для Photos
4. `done.list` щоб не копіювати те саме знову

## Відмова від відповідальності

Освітній і практичний матеріал. Перевіряйте під ваші compliance, cost і SLO перед production.

## Контакти

- Portfolio: https://boryslavdeputat.com/
- ClawDBot / KLAV (UA AI): https://clawdbot.llc/
- Email: info@boryslavdeputat.com

## Ліцензія

MIT - див. [LICENSE](LICENSE).
