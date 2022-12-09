import os
import subprocess

import pytest
import virtualenv


PATCH_VERSIONS = ["1", "2"]


@pytest.fixture(scope="module", params=PATCH_VERSIONS)
def asdf_version(request):
    """
    The (old) version of the asdf library under test.
    """
    return request.param


def env_run(env_path, command, *args, **kwargs):
    """
    Run a command on the context of the virtual environment at
    the specified path.
    """
    print(f"env_run({env_path}, {command}, {args}, {kwargs})")
    kwargs["bufsize"] = 0
    #return subprocess.run([env_path / "bin" / command] + list(args), **kwargs).returncode == 0


@pytest.fixture(scope="module")
def env_path(asdf_version, tmp_path_factory):
    """
    Path to the virtualenv where the (old) asdf library is installed.
    """
    path = tmp_path_factory.mktemp(f"asdf-{asdf_version}-env", numbered=False)
    print(f"env_path {asdf_version} {path}")

    virtualenv.cli_run([str(path)])

    env_run(path, "python3", "--version")
    # env_run(path, "pip", "install", "requests")
    # assert env_run(path, "pip", "install", f"asdf=={asdf_version}"), f"Failed to install asdf version {asdf_version}"
    return path


def test_run_subprocess(asdf_version):
    print("do nothing")
