import pytest
import virtualenv


@pytest.mark.parametrize("version", ["1", "2"])
def test_run_virtualenv(version):
    path = f".tmp_{version}"
    virtualenv.cli_run([str(path)])
