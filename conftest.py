def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default=None, help="Platform to run tests on (android or ios)"
    )
