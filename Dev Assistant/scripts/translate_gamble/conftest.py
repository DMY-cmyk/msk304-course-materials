import sys
from pathlib import Path

# Make the parent dir importable so `from translate_gamble import ...` works
_PARENT = Path(__file__).resolve().parent.parent
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))
