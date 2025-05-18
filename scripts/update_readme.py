import requests, re

# 1. Fetch a random quote from ZenQuotes
#    ZenQuotes returns a list of objects: [{"q":"Quote","a":"Author"}]
resp = requests.get("https://zenquotes.io/api/random").json()
quote_text = resp[0]['q']
quote_author = resp[0]['a']
quote = f"“{quote_text}” — {quote_author}"

# 2. Prepare the live GitHub stats badge
stats_badge = (
    "![Stats]"
    "(https://github-readme-stats.vercel.app/api?"
    "username=RiyaGupta2230&show_icons=true&theme=radical)"
)

# 3. Load the README template and replace placeholders
with open("README.template.md", "r", encoding="utf-8") as f:
    template = f.read()

readme = (
    template
    .replace("{{QUOTE}}", quote)
    .replace("{{STATS_BADGE}}", stats_badge)
)

# 4. Write out the final README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
