import subprocess

import pytest


@pytest.mark.parametrize("msg", ["1", "2"])
def test_run_subprocess(msg):
    assert subprocess.run(["python3", "-c", f"'print({msg})'"]).returncode == 0
