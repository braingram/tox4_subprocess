import pytest
import virtualenv


# PATCH_VERSIONS = ["1", "2"]
# 
# 
# @pytest.fixture(scope="module", params=PATCH_VERSIONS)
# def asdf_version(request):
#     return request.param


# @pytest.fixture(scope="module")
# def env_path(asdf_version):
#     path = ".tmp"
#     virtualenv.cli_run([str(path)])
#     #return path


#def test_run_subprocess(asdf_version, env_path):
@pytest.mark.parametrize("asdf_version", ["1", "2"])
def test_run_subprocess(asdf_version):
    path = f".tmp_{asdf_version}"
    virtualenv.cli_run([str(path)])
    print("do nothing")
