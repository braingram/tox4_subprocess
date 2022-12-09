import pytest
import virtualenv


PATCH_VERSIONS = ["1", "2"]


@pytest.fixture(scope="module", params=PATCH_VERSIONS)
def asdf_version(request):
    return request.param


@pytest.fixture(scope="module")
def env_path(asdf_version):
    #path = tmp_path_factory.mktemp(f"asdf-{asdf_version}-env", numbered=False)
    path = ".tmp"
    virtualenv.cli_run([str(path)])
    #return path


def test_run_subprocess(asdf_version, env_path):
    print("do nothing")
