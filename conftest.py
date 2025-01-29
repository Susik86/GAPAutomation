def pytest_addoption(parser):
    parser.addoption(
        "--platform",  # Պլատֆորմի անունը
        action="store",
        default="android",  # Default արժեք, եթե ոչինչ չի փոխանցվում
        help="Platform to run tests on: android or ios",  # Օգնության նկարագրություն
    )
