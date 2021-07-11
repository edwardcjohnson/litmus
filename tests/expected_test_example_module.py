
import pytest

class TestClassAddition():

    @pytest.mark.parametrize(
        "params,expected",
        [
            [
                {
                    'a': 3,
					'b': 3
                },
                9
            ]
        ]
    )
    def test_return(self, params, expected):
        import tests.example_module as example_module
        assert example_module.Arithmetic().addition(params['a'], params['b']) == expected

class TestClassDivision():

    @pytest.mark.parametrize(
        "params,expected",
        [
            [
                {
                    'a': 3,
					'b': 3
                },
                9
            ]
        ]
    )
    def test_return(self, params, expected):
        import tests.example_module as example_module
        assert example_module.Arithmetic().division(params['a'], params['b']) == expected

class TestClassMultiplication():

    @pytest.mark.parametrize(
        "params,expected",
        [
            [
                {
                    'a': 3,
					'b': 3
                },
                9
            ]
        ]
    )
    def test_return(self, params, expected):
        import tests.example_module as example_module
        assert example_module.Arithmetic().multiplication(params['a'], params['b']) == expected

class TestClassSubtraction():

    @pytest.mark.parametrize(
        "params,expected",
        [
            [
                {
                    'a': 3,
					'b': 3
                },
                9
            ]
        ]
    )
    def test_return(self, params, expected):
        import tests.example_module as example_module
        assert example_module.Arithmetic().subtraction(params['a'], params['b']) == expected
