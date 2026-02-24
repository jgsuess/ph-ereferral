#!/bin/sh
# convert-to-fsh.sh — Convert validated FHIR JSON examples to FSH
# using GoFSH, then post-process the output for IG integration.
#
# Usage:
#   ./utils/convert-to-fsh.sh
#
# Prerequisites:
#   - Node.js + npm
#   - GoFSH installed globally (npm install -g gofsh) or locally

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
INPUT_DIR="$REPO_ROOT/input/examples-json-source"
GOFSH_OUTPUT="$REPO_ROOT/input/examples-json-source/gofsh-output"
FSH_TARGET="$REPO_ROOT/input/fsh/examples"

# Check gofsh is available
if command -v gofsh >/dev/null 2>&1; then
    GOFSH="gofsh"
elif [ -x "$REPO_ROOT/node_modules/.bin/gofsh" ]; then
    GOFSH="$REPO_ROOT/node_modules/.bin/gofsh"
else
    echo "GoFSH not found. Installing locally..."
    cd "$REPO_ROOT" && npm install gofsh
    GOFSH="$REPO_ROOT/node_modules/.bin/gofsh"
fi

echo "=== Converting JSON examples to FSH ==="
echo "Input:  $INPUT_DIR"
echo "Output: $GOFSH_OUTPUT"
echo ""

# Clean previous output
rm -rf "$GOFSH_OUTPUT"
mkdir -p "$GOFSH_OUTPUT"

# Run GoFSH on all *-ex.json files
# Copy JSON files to a temp dir to avoid non-json files confusing gofsh
TMPDIR=$(mktemp -d)
cp "$INPUT_DIR"/*-ex.json "$TMPDIR/" 2>/dev/null || true

$GOFSH "$TMPDIR" -o "$GOFSH_OUTPUT" -s "$REPO_ROOT" 2>&1 || true

rm -rf "$TMPDIR"

echo ""
echo "=== Post-processing FSH files ==="

# Use venv python if available
if [ -f "$REPO_ROOT/.venv/bin/python" ]; then
    PYTHON="$REPO_ROOT/.venv/bin/python"
else
    PYTHON="python3"
fi

# Post-process: fix profile names, add DD annotations, copy to target
$PYTHON -c "
import os, glob, re

gofsh_dir = '$GOFSH_OUTPUT'
target_dir = '$FSH_TARGET'
os.makedirs(target_dir, exist_ok=True)

# Profile URL -> FSH alias mapping
profile_map = {
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-patient': 'PHCorePatient',
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-encounter': 'PHCoreEncounter',
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-observation': 'PHCoreObservation',
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-organization': 'PHCoreOrganization',
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-practitioner': 'PHCorePractitioner',
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-medication': 'PHCoreMedication',
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-relatedperson': 'PHCoreRelatedPerson',
    'http://doh.gov.ph/fhir/ph-core/StructureDefinition/ph-core-procedure': 'PHCoreProcedure',
}

count = 0
for fsh_file in sorted(glob.glob(os.path.join(gofsh_dir, '**', '*.fsh'), recursive=True)):
    with open(fsh_file, 'r') as f:
        content = f.read()
    
    # Replace profile URLs with FSH names in InstanceOf
    for url, name in profile_map.items():
        content = content.replace(f'InstanceOf: {url}', f'InstanceOf: {name}')
    
    # Ensure Usage: #example is present
    if 'Usage:' not in content:
        content = content.replace('InstanceOf:', 'Usage: #example\nInstanceOf:', 1)
    
    # Write to target
    basename = os.path.basename(fsh_file)
    target_path = os.path.join(target_dir, basename)
    with open(target_path, 'w') as f:
        f.write(content)
    count += 1
    print(f'  ✓ {basename}')

if count == 0:
    print('  (no FSH files generated — GoFSH may have produced output in a different structure)')
    # List what was generated
    for root, dirs, files in os.walk(gofsh_dir):
        for fn in files:
            print(f'    found: {os.path.relpath(os.path.join(root, fn), gofsh_dir)}')
else:
    print(f'')
    print(f'✓ {count} FSH files copied to {target_dir}')
"

echo ""
echo "=== Done ==="
echo "FSH examples are in: $FSH_TARGET"
echo "GoFSH raw output in: $GOFSH_OUTPUT"
echo ""
echo "Next steps:"
echo "  1. Review generated FSH files"
echo "  2. Author transaction bundle FSH files (registration + ANC contact)"
echo "  3. Run SUSHI to compile: ./_genonce.sh"
