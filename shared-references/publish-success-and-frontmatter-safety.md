# Publish Success and Frontmatter Safety

This file defines cross-collection rules for when a posting workflow may claim success, and how frontmatter strings should be written safely.

## 1. Success-claim rule

Do not collapse these states into one vague “done” message.
They are different:

1. files changed locally
2. local validation / parsing passed
3. local build/check passed when relevant
4. commit / push completed
5. remote deployment/build status is confirmed safe when relevant

## Allowed language by state

### Only files changed locally
Allowed:
- `已经改好了，正在校验。`
- `文件已更新，下一步检查 build / frontmatter。`

Not allowed:
- `好了`
- `已经可以用了`
- `已经上线了`

### Local validation/build passed, but not pushed yet
Allowed:
- `本地已通过校验，正在提交 / 推送。`

Not allowed:
- `已经 push 好了`
- `远端已经可见`

### Pushed, but remote deployment/build not yet confirmed
Allowed:
- `已经 push，正在等远端构建结果。`
- `代码已上去，等部署确认后再算完全完成。`

Not allowed:
- `已经完全好了`
- `现在网站已经可用了`

### Only after relevant checks are complete
Only then may the workflow say things like:
- `这次改动已经完成。`
- `远端已经正常。`
- `现在可以正常访问。`

## Operational rule

When in doubt, report the more conservative status.
Do not over-claim completion.

## 2. Frontmatter string safety rule

When writing frontmatter strings, prefer safe quoting whenever the value might confuse YAML parsing.

### Quote by default when a string contains:
- `:` colon
- quotes
- leading/trailing whitespace risk
- hash-like fragments or punctuation that may be misread
- complex multilingual punctuation

### Especially watch fields like:
- `title`
- `description`
- `location`
- `author`

## Recommended rule of thumb

If a frontmatter string would make you pause and wonder whether YAML might parse it strangely, quote it.

Safer example:

```yaml
title: "Munich to Venice: Solo Crossing Notes"
```

Instead of:

```yaml
title: Munich to Venice: Solo Crossing Notes
```

## 3. Multilingual completion rule

When multiple language files are being updated:
- do not claim all language outputs are ready until all of them pass the relevant checks
- do not let one successful language file stand in for the whole set

Use language like:
- `zh 已好，正在补 en/de。`
- `三语文件已改完，正在统一校验。`
- `三语都已通过本地检查。`

## 4. Preferred discipline

For collection-posting workflows:
- write/update files
- verify frontmatter safety
- run relevant local validation/build checks
- commit/push
- confirm remote status when relevant
- only then claim full success
