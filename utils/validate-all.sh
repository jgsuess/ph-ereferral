#!/bin/sh
# validate-all.sh — Validate all *-ex.json files in input/examples/
# against a FHIR server using the existing fhir-validate.py script.
#
# Usage:
#   ./utils/validate-all.sh [FHIR_SERVER_URL]
#
# Default server: http://localhost:8080/fhir  (local HAPI FHIR)
#
# Prerequisites:
#   - Python 3 with 'requests' installed
#   - A running FHIR R4 server (e.g. docker run -p 8080:8080 hapiproject/hapi)

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
INPUT_DIR="$REPO_ROOT/input/examples-json-source"
OUTPUT_DIR="$REPO_ROOT/input/examples-json-source/validation-results"
FHIR_SERVER="${1:-http://localhost:8080/fhir}"

# Use venv python if available
if [ -f "$REPO_ROOT/.venv/bin/python" ]; then
    PYTHON="$REPO_ROOT/.venv/bin/python"
else
    PYTHON="python3"
fi

# Ensure requests is installed
$PYTHON -c "import requests" 2>/dev/null || {
    echo "Installing 'requests' package..."
    $PYTHON -m pip install requests
}

# Check server is reachable
echo "Checking FHIR server at $FHIR_SERVER ..."
if ! $PYTHON -c "
import requests, sys
try:
    r = requests.get('$FHIR_SERVER/metadata', timeout=5)
    if r.status_code == 200:
        print('  ✓ Server is reachable')
    else:
        print(f'  ✗ Server returned status {r.status_code}')
        sys.exit(1)
except Exception as e:
    print(f'  ✗ Cannot reach server: {e}')
    sys.exit(1)
"; then
    echo ""
    echo "To start a local HAPI FHIR server:"
    echo "  docker run -d -p 8080:8080 hapiproject/hapi"
    exit 1
fi

echo ""
echo "Validating all *-ex.json files in $INPUT_DIR ..."
echo "Results will be saved to $OUTPUT_DIR"
echo ""

$PYTHON "$SCRIPT_DIR/fhir-validate.py" "$FHIR_SERVER" "$INPUT_DIR" "$OUTPUT_DIR"

# Parse results and print summary
echo ""
echo "=== Validation Summary ==="
$PYTHON -c "
import os, json, glob

results_dir = '$OUTPUT_DIR'
passed = 0
failed = 0
errors_list = []

for f in sorted(glob.glob(os.path.join(results_dir, '*-response.json'))):
    try:
        with open(f) as fh:
            data = json.load(fh)
        issues = data.get('issue', [])
        errs = [i for i in issues if i.get('severity') in ('error', 'fatal')]
        name = os.path.basename(f).replace('-response.json', '')
        if errs:
            failed += 1
            errors_list.append((name, errs))
            print(f'  ✗ {name}: {len(errs)} error(s)')
        else:
            passed += 1
            warns = [i for i in issues if i.get('severity') == 'warning']
            print(f'  ✓ {name}' + (f' ({len(warns)} warning(s))' if warns else ''))
    except Exception as e:
        failed += 1
        print(f'  ? {os.path.basename(f)}: could not parse response ({e})')

print(f'')
print(f'Passed: {passed}  Failed: {failed}  Total: {passed + failed}')

if errors_list:
    print(f'')
    print('--- Errors Detail ---')
    for name, errs in errors_list:
        print(f'')
        print(f'{name}:')
        for e in errs:
            loc = e.get('expression', [e.get('location', ['?'])])[0] if isinstance(e.get('expression'), list) else e.get('expression', '?')
            print(f'  [{e.get(\"severity\")}] {loc}: {e.get(\"diagnostics\", \"\")}')
"

echo ""
echo "Done. Full responses in $OUTPUT_DIR"
