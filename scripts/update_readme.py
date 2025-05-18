import requests, re

# 1. Fetch a random chai quote
resp = requests.get("https://api.quotable.io/quotes/random").json()  # GET /quotes/random :contentReference[oaicite:8]{index=8}
quote = f"“{resp['content']}” — {resp['author']}"

# 2. Prepare the live GitHub stats badge
stats_badge = "![Stats](https://github-readme-stats.vercel.app/api?username=RiyaGupta2230&show_icons=true&theme=radical)"  # theme=radical :contentReference[oaicite:9]{index=9}

# 3. Load and fill template
with open("README.template.md", "r", encoding="utf-8") as f:
    tmpl = f.read()
readme = tmpl.replace("{{QUOTE}}", quote).replace("{{STATS_BADGE}}", stats_badge)

# 4. Write final README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
