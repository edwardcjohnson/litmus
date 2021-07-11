import pytest
import filecmp
import litmus.compose
import os
import pathlib
this_path = pathlib.Path(__file__).parent.resolve()

class TestClassComposeTestModuleSkeleton():

    @pytest.mark.parametrize(
        "params,expected",
        [
            [
                {
                    'module_file': "example_module.py"
                },
                "expected_test_example_module.py"
            ]
        ]
    )
    def test_return(self, params, expected):
        litmus.compose.compose_test_module_skeleton(params["module_file"])
        actual_test_example_module = "test_example_module.py"
        assert filecmp.cmp(
            f"{this_path}/{expected}",
            actual_test_example_module,
            shallow=False
        )

        # Clean up test dir, by deleting the generated test module.
        # You can keep the generated test module if you want to
        # pytest it on the next pytest run.
        # If file exists, delete it
        if os.path.isfile(actual_test_example_module):
            os.remove(actual_test_example_module)
        else:
            print(f"Error: {actual_test_example_module} file not found")