---
name: caddy-local-proxy
description: "Explains the shared Caddy reverse proxy setup used across local development projects on this machine."
---

# Skill Name: Caddy Local HTTPS Proxy

## 🎯 Objective
Explains the shared Caddy reverse proxy setup used across local development projects on this machine. Provides the mental model, day-to-day commands, and patterns for registering new projects — so any Claude session or developer can operate or extend the proxy without re-discovering how it works.

## 👤 Target Persona
Developer (or Claude Code) adding a new project, debugging a broken local domain, or extending the proxy to serve a new `*.localhost` domain.

---

## 📐 Mental Model

One `caddy` process owns port 443 on the machine. It reads a master config file that **imports per-project snippet files** from a shared directory. Each project is responsible only for its own snippet; the daemon starts/reloads automatically when a snippet is registered.

```
~/.config/caddy/
├── Caddyfile                  ← master (auto-bootstrapped; do not edit by hand)
├── register.sh                ← add/update a project snippet → start or reload Caddy
├── unregister.sh              ← remove a project snippet → reload or stop Caddy
└── sites/
    ├── agentic-pdlc.caddy     ← Agentic PDLC domains
    ├── personal-assistant.caddy
    └── <future-project>.caddy
```

**TLS** is handled automatically. The master Caddyfile uses `local_certs` — Caddy's built-in local CA generates and auto-renews certificates for any `*.localhost` domain. No `mkcert`, no manual cert files. The CA is trusted system-wide via `caddy trust` (run once, already done).

---

## 📥 Inputs Required

When registering a new project:
- **Domain(s)**: the `*.localhost` hostname(s) the project should answer on
- **Backend port**: the port the API/backend process listens on (e.g. `8000`)
- **Frontend port** (if applicable): the port the dev server listens on (e.g. `3000`)
- **Routing rules**: whether the project uses path-based routing (e.g. `/api/*` → backend, everything else → frontend) or host-based routing (separate subdomains per service)

---

## 📤 Expected Output

After registration:
- `https://<your-domain>.localhost` is reachable in the browser with a valid cert (no warnings)
- `https://<your-domain>.localhost/api/health` (or equivalent) returns 200
- Other registered projects are unaffected — `lsof -i :443` shows exactly one `caddy` PID

---

## 🛠 Day-to-Day Commands

### Check whether Caddy is running
```bash
curl -s http://localhost:2019/config/ | python3 -m json.tool | head -20
# Returns JSON if running; "connection refused" if not
```

### See all registered domains
```bash
curl -s http://localhost:2019/config/ | python3 -c "
import json,sys
cfg = json.load(sys.stdin)
routes = cfg.get('apps',{}).get('http',{}).get('servers',{}).get('srv0',{}).get('routes',[])
for r in routes:
    for m in r.get('match',[]):
        hosts = m.get('host',[])
        if hosts: print('Domain:', hosts)
"
```

### Register a project (start or reload)
```bash
bash ~/.config/caddy/register.sh /path/to/project/snippet.caddy
```

### Unregister a project
```bash
bash ~/.config/caddy/unregister.sh <site-name>   # e.g. "agentic-pdlc" (no .caddy extension)
```

### Reload after manually editing a snippet
```bash
caddy reload --config ~/.config/caddy/Caddyfile
```

### Stop Caddy entirely
```bash
caddy stop
```

### Restart from scratch
```bash
caddy stop
bash ~/.config/caddy/register.sh /path/to/any-snippet.caddy
```

### Check which process owns port 443
```bash
lsof -i :443 | grep LISTEN
# Should show exactly one caddy PID
```

### Trust the local CA (only needed once per machine, or after re-install)
```bash
caddy start --config ~/.config/caddy/Caddyfile && caddy trust
```

---

## 🆕 Adding a New Project (step-by-step)

### Step 1 — Add `/etc/hosts` entries
```bash
sudo sh -c 'echo "127.0.0.1 myproject.localhost" >> /etc/hosts'
sudo sh -c 'echo "127.0.0.1 api.myproject.localhost" >> /etc/hosts'
sudo dscacheutil -flushcache   # flush DNS cache on macOS
```

### Step 2 — Create a `.caddy` snippet in the project repo

**Pattern A — path-based routing (frontend + backend on one domain):**
```caddy
myproject.localhost {
    handle /api/* {
        uri strip_prefix /api
        reverse_proxy localhost:8000
    }
    handle {
        reverse_proxy localhost:3000
    }
}
```

**Pattern B — host-based routing (separate subdomain per service):**
```caddy
myproject.localhost {
    reverse_proxy localhost:3000
}

api.myproject.localhost {
    reverse_proxy localhost:8000
}
```

**Pattern C — backend only (no frontend, e.g. a microservice or CLI tool):**
```caddy
myproject.localhost {
    reverse_proxy localhost:8000
}
```

> **Rules for snippet files:**
> - No global block `{ ... }` — that belongs only in the master `Caddyfile`
> - No `tls` directive — `local_certs` in the master handles it
> - Use tab indentation (Caddy's formatter enforces this)
> - Name the file `<project-slug>.caddy` (lowercase, hyphens OK)

### Step 3 — Call `register.sh` from the project's start script
```bash
bash ~/.config/caddy/register.sh "${SCRIPT_DIR}/myproject.caddy"
```

### Step 4 — Optionally call `unregister.sh` from the project's stop script
```bash
bash ~/.config/caddy/unregister.sh myproject
```

### Step 5 — Verify
```bash
curl -sk https://myproject.localhost/health   # or whatever the health endpoint is
```

---

## 🔍 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `curl: (7) Failed to connect` | Caddy not running | `bash ~/.config/caddy/register.sh <any-snippet>` |
| `curl: (35) SSL handshake failed` | Stale Caddy daemon from another project | `caddy stop && bash ~/.config/caddy/register.sh <snippet>` |
| `curl: (6) Could not resolve host` | Missing `/etc/hosts` entry | Add `127.0.0.1 <domain>` to `/etc/hosts` |
| Browser shows "NET::ERR_CERT_AUTHORITY_INVALID" | Local CA not trusted | `caddy trust` (Caddy must be running first) |
| Domain 404 / wrong project responds | Two Caddy instances running | `caddy stop`, then re-register via `register.sh` |
| `No files matching import glob pattern` | Snippet not in `sites/` yet | `register.sh` copies the snippet before reloading |
| Port 443 refused after `caddy stop` + `caddy start --config Caddyfile` | Started without `--config`, used autosave | Always pass `--config ~/.config/caddy/Caddyfile` explicitly, or use `register.sh` |

### The autosave trap
Caddy saves its last config to `~/Library/Application Support/Caddy/autosave.json`. If you run `caddy start` without `--config`, it loads the autosave — which may be from a different project. **Always use `register.sh` or pass `--config` explicitly.**

---

## ✅ Success Criteria / Quality Checklist

- [ ] `lsof -i :443 | grep LISTEN` shows exactly **one** `caddy` PID
- [ ] `curl -sk https://<domain>/` returns expected content for each registered project
- [ ] Registering a second project does not break the first
- [ ] `caddy stop` on one project's domains does not kill the proxy for other projects (only `unregister.sh` or explicit `caddy stop` does that)
- [ ] No browser TLS warnings on any `*.localhost` domain

---

## 🏗 Architecture Reference

### Master Caddyfile (`~/.config/caddy/Caddyfile`)
```caddy
{
	local_certs
	admin localhost:2019
}

import /Users/<you>/.config/caddy/sites/*.caddy
```
> This file is auto-created by `register.sh`. Do not edit by hand — the import path uses the absolute home directory path (not `~`) because Caddy does not expand tildes in `import` directives.

### `register.sh` logic
1. Creates `~/.config/caddy/sites/` if missing
2. Bootstraps the master `Caddyfile` if it doesn't exist yet
3. Copies the snippet to `sites/`
4. If Caddy is already running (detects via admin API): `caddy reload`
5. If Caddy is not running: `caddy start` → `caddy trust`

### `unregister.sh` logic
1. Removes the snippet from `sites/`
2. If other snippets remain: `caddy reload`
3. If no snippets remain: `caddy stop`

---

**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-06
- **Author:** northernfried
- **Applies to:** macOS, Caddy v2, `*.localhost` domains
