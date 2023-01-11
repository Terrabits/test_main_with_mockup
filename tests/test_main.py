from project          import main  # main module
from project.mock.fsw import Fsw   # mock fsw
from unittest         import TestCase


# use mock fsw for testing
main.Fsw = Fsw


class TestMain(TestCase):

    def test_main(self):
        main.main()
