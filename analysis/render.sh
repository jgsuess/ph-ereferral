#!/usr/bin/env bash
# Render analysis/spec-holes.md → spec-holes.html + spec-holes.pdf
# with PlantUML diagrams rendered inline.
#
# Usage:  cd analysis && bash render.sh
# Output: spec-holes.html  spec-holes.pdf  (same directory)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ── Step 1: render PlantUML diagrams to PNG ────────────────────────────────────
echo "=== Step 1: render PlantUML diagrams to PNG ==="
mkdir -p diagrams/rendered
for f in diagrams/*.puml; do
  name=$(basename "$f" .puml)
  out="diagrams/rendered/${name}.png"
  echo "  $f"
  plantuml -tpng -o "$(pwd)/diagrams/rendered" "$f" 2>/dev/null && echo "    → $out" || echo "    WARNING: failed, skipping"
done

# ── Step 2: inject diagram images into a working copy of the markdown ──────────
echo ""
echo "=== Step 2: inject diagram images ==="
python3 - <<'PYEOF'
import re, os

with open("spec-holes.md", "r") as f:
    content = f.read()

# After any line containing "analysis/diagrams/X.puml" insert an image tag
# if a rendered PNG exists for that diagram.
def maybe_insert_image(m):
    stem = m.group(1)
    png = f"diagrams/rendered/{stem}.png"
    ref = m.group(0)
    if os.path.exists(png):
        return ref + f"\n\n![{stem}]({png})\n"
    return ref

content = re.sub(
    r'`analysis/diagrams/([\w-]+)\.puml`',
    maybe_insert_image,
    content
)

with open("spec-holes-work.md", "w") as f:
    f.write(content)
print("  done")
PYEOF

# ── Step 3: write CSS to a temp file ──────────────────────────────────────────
CSS_FILE=$(mktemp /tmp/spec-holes-XXXXXX.css)
cat > "$CSS_FILE" <<'CSSEOF'
body {
  font-family: "Helvetica Neue", Arial, sans-serif;
  max-width: 960px; margin: 0 auto; padding: 2em;
  line-height: 1.65; color: #222; font-size: 15px;
}
h1 { color: #B71C1C; border-bottom: 3px solid #B71C1C; padding-bottom: 0.3em; margin-top: 1em; }
h2 { color: #1A237E; border-bottom: 1px solid #9FA8DA; padding-bottom: 0.2em; margin-top: 2em; }
h3 { color: #1B5E20; margin-top: 1.5em; }
h4 { color: #37474F; margin-top: 1.2em; }
#TOC { background: #F5F5F5; border: 1px solid #DDD; padding: 1em 1.5em;
       border-radius: 6px; margin-bottom: 2em; }
#TOC a { color: #1A237E; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.88em; }
th { background: #1A237E; color: white; padding: 8px 12px; text-align: left; }
td { border: 1px solid #C5CAE9; padding: 6px 12px; vertical-align: top; }
tr:nth-child(even) td { background: #E8EAF6; }
code { background: #F5F5F5; border: 1px solid #E0E0E0; border-radius: 3px;
       padding: 1px 5px; font-size: 0.88em; }
pre { background: #263238; color: #ECEFF1; border-radius: 6px;
      padding: 1.2em; overflow-x: auto; font-size: 0.82em; line-height: 1.45; }
pre code { background: none; border: none; color: inherit; padding: 0; font-size: inherit; }
img { max-width: 100%; border: 1px solid #DDD; border-radius: 4px;
      margin: 1.2em 0; display: block; box-shadow: 0 2px 6px rgba(0,0,0,0.12); }
blockquote { border-left: 4px solid #9FA8DA; margin: 1em 0; padding: 0.6em 1em;
             background: #EEF2FF; color: #333; border-radius: 0 4px 4px 0; }
hr { border: none; border-top: 1px solid #E0E0E0; margin: 2.5em 0; }
a { color: #1565C0; }
CSSEOF

# ── Step 4: pandoc → self-contained HTML ──────────────────────────────────────
echo ""
echo "=== Step 3: pandoc → HTML ==="
pandoc spec-holes-work.md \
  --standalone \
  --self-contained \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --metadata title="PH eReferral v0.1 — Specification Holes and Counter-Intuitive Sequences" \
  --metadata date="2026-06-17" \
  --metadata author="Branch: worktree-spec-holes-analysis" \
  --highlight-style=tango \
  --css="$CSS_FILE" \
  -o spec-holes.html
echo "  → spec-holes.html"

rm -f "$CSS_FILE"

# ── Step 5: pandoc → PDF via xelatex ──────────────────────────────────────────
echo ""
echo "=== Step 4: pandoc → PDF ==="
pandoc spec-holes-work.md \
  --standalone \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --pdf-engine=xelatex \
  --metadata title="PH eReferral v0.1 — Specification Holes" \
  --metadata date="2026-06-17" \
  --metadata author="Branch: worktree-spec-holes-analysis" \
  -V geometry:margin=2.2cm \
  -V fontsize=10pt \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V toccolor=blue \
  -V mainfont="DejaVu Serif" \
  -V monofont="DejaVu Sans Mono" \
  --highlight-style=tango \
  -o spec-holes.pdf 2>&1 | grep -v "^$" | tail -8 \
  && echo "  → spec-holes.pdf" \
  || echo "  WARNING: PDF failed — check xelatex. HTML is complete."

# ── Cleanup ───────────────────────────────────────────────────────────────────
rm -f spec-holes-work.md

echo ""
echo "=== Done ==="
echo "  HTML: $(pwd)/spec-holes.html"
echo "  PDF:  $(pwd)/spec-holes.pdf"
