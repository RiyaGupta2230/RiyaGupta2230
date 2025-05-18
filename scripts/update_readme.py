import requests, random, os

# 1. Fetch a random chai-worthy quote every hour
resp = requests.get("https://zenquotes.io/api/random").json()
quote = f"“{resp[0]['q']}” — {resp[0]['a']}"  # :contentReference[oaicite:11]{index=11}

# 2. Prepare badges & stats
stats_badge = (
    "![Stats]"
    "(https://github-readme-stats.vercel.app/api?"
    "username=RiyaGupta2230&show_icons=true&theme=radical)"
)

# 3. Generate a random tic-tac-toe board

# Generate a random tic-tac-toe board (now with chai & biscuit!)
symbols = ['🍵', '🍪', '▫️']  # 🍵 = chai, 🍪 = biscuit, ▫️ = blank

board = []
for _ in range(3):
      row = [random.choice(symbols) for _ in range(3)]
      board.append(" ".join(row))
ttt_section = "```\n" + "\n".join(board) + "\n```"


# 4. Load template & replace all placeholders
script_dir = os.path.dirname(__file__)                 # e.g. ".../scripts"
template_path = os.path.join(script_dir, "../README.template.md")
with open(template_path, "r", encoding="utf-8") as f:
     tpl = f.read()

readme = (
    tpl
    .replace("{{QUOTE}}", quote)
    .replace("{{STATS_BADGE}}", stats_badge)
    .replace("{{TICTACTOE}}", ttt_section)
)

# 5. Write out final README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
