# Event Asset Rules

Event assets must follow ACC repo governance.

## Asset classes in Phase 1

- cover image
- WeChat QR image
- gallery images

## Target paths

### Cover
```text
frontend/public/images/events/{slug}/cover.jpg
```
Referenced as:
```yaml
cover: /images/events/{slug}/cover.jpg
```

### WeChat QR
```text
frontend/public/images/events/{slug}/wechat-qr.png
```
Referenced as:
```yaml
wechatQrCode: /images/events/{slug}/wechat-qr.png
```

### Gallery
```text
frontend/public/images/events/{slug}/gallery/01-descriptor.jpg
frontend/public/images/events/{slug}/gallery/02-descriptor.jpg
```
Referenced in markdown body as absolute paths.

## Naming rules

- lowercase only
- hyphen-separated
- two-digit gallery ordering
- no spaces, no underscores, no UUID-like names

## Operational rule

Assets first, markdown second.

Do not finalize markdown references until asset names and target paths are stable.

## Preview rule

During Telegram preview stage, include an asset summary:
- chosen cover
- QR present or missing
- gallery count
- final planned asset names
