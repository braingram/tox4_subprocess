import subprocess

import pytest


@pytest.mark.parametrize("msg", ["1", "2"])
def test_run_subprocess(msg):
    assert subprocess.run(["echo", str(msg)]).returncode == 0
