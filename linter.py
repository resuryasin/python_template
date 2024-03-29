import sys
import os
sys.path.append(os.path.join(os.getcwd(), "package_name"))

from pylint import lint

THRESHOLD = 9

run = lint.Run(["package_name"], do_exit=False)
score = run.linter.stats.global_note

if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)

sys.exit(0)
