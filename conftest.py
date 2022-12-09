# import os
# 
# import pytest
# 
# 
# @pytest.fixture(scope="session", autouse=True)
# def temp_cwd(tmpdir_factory):
#     """
#     This fixture creates a temporary current working directory
#     for the test session, so that docstring tests that write files
#     don't clutter up the real cwd.
#     """
#     original_cwd = os.getcwd()
#     try:
#         path = tmpdir_factory.mktemp("cwd")
#         print(f"temp_cwd {path} {original_cwd}")
#         os.chdir(path)
#         # os.chdir(tmpdir_factory.mktemp("cwd"))
#         yield
#     finally:
#         print(f"-- temp_cwd back to {original_cwd}")
#         os.chdir(original_cwd)
