import subprocess

import pytest
import pytest_remotedata
import virtualenv


@pytest.mark.parametrize("msg", ["1", "2"])
def test_run_subprocess(msg, tmp_path_factory):
    path = tmp_path_factory.mktemp(f"foo_{msg}", numbered=False)

    virtualenv.cli_run([str(path)])

    assert subprocess.run([path / "bin" / "python", "--version"]).returncode == 0
