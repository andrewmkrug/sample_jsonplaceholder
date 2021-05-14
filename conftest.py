import pytest
import logging
import json

from config import TestCase, Config


@pytest.fixture(scope='function')
def test_case(test_run, py_config, request) -> TestCase:
    """ Manages data pertaining to the currently running Test Function or Case.
        * Creates the test-specific logger.
    Args:
        test_run: The Test Run (or Session) this test is connected to.
    Returns:
        An instance of TestCase.
    """
    test_name = request.node.name
    test_result_path = f'{test_run}/{test_name}'
    py_config.driver.capabilities.update({'name': test_name})
    return TestCase(name=test_name, file_path=test_result_path)


@pytest.fixture(scope='session')
def py_config(project_root, request) -> Config:
    """ Initialize a PyleniumConfig for each test
    1. This starts by deserializing the user-created pylenium.json from the Project Root.
    2. If that file is not found, then proceed with Pylenium Defaults.
    3. Then any CLI arguments override their respective key/values.
    """
    try:
        # 1. Load pylenium.json in Project Root, if available
        with open(f'{project_root}/config.json') as file:
            _json = json.load(file)
        config = Config(**_json)
    except FileNotFoundError:
        # 2. pylenium.json not found, proceed with defaults
        config = Config()

    # Logging Settings
    cli_pylog_level = request.config.getoption('--pylog_level')
    if cli_pylog_level:
        config.logging.pylog_level = cli_pylog_level


    return config