import subprocess

import pytest
import virtualenv


@pytest.mark.parametrize("version", ["0", "1", "2"])
def test_run_virtualenv(version):
    path = f".tmp_{version}"
    virtualenv.cli_run([str(path)])
    #assert subprocess.run(["virtualenv", str(path)]).returncode == 0
