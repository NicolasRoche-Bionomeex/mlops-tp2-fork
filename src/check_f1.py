"""Bonus, cycle 4: fail the CI when the model is too weak.

    python tools/check_f1.py

Reads metrics.json, written by the evaluate stage. A CI step that exits with a
non-zero code turns the whole job red.
"""
import json
import sys

THRESHOLD = 0.75 

f1 = json.load(open("metrics.json"))["f1"]

print(f"f1 = {f1}  (threshold {THRESHOLD})")

sys.exit(0 if f1 >= THRESHOLD else 1)

##### cycle 4, bonus : sortez avec le code 0 si f1 >= THRESHOLD, 1 sinon (sys.exit)
