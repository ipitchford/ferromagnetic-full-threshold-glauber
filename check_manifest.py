import hashlib, json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for row in manifest['files']:
    p=root/row['path']
    if p.stat().st_size!=row['size_bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
        raise SystemExit('Manifest mismatch: '+row['path'])
print('PASS manifest',len(manifest['files']))
