from lib.solutions.CHK import checkout_solution


class TestChk:
    def test_checkout(self):
        assert checkout_solution.checkout("3A,2A") == 330
        assert checkout_solution.checkout("A,D") == 65

