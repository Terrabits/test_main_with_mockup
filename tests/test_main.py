from project          import main  # main module
from project.mock.fsw import MockFsw   # mock fsw
from unittest         import TestCase


# use mock fsw for testing
print('in module tests.test_main')
print('replacing project.main.Fsw with MockFsw')
main.Fsw = MockFsw


class TestMain(TestCase):

    def test_main(self):
        main.main()
