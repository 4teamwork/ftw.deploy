from pytest_console_scripts import ScriptRunner
from pytest_console_scripts import script_cwd
import pytest


@pytest.fixture(scope='class', autouse=True)
def script_runner(request):
    request.cls.script_runner = ScriptRunner('subprocess', script_cwd).run
