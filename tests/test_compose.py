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
            f"{this_path}/expected_test_example_module.py",
            actual_test_example_module,
            shallow=False
        )

        # clean up test dir, by deleting the generated test_module
        # If file exists, delete it
        if os.path.isfile(actual_test_example_module):
            os.remove(actual_test_example_module)
        else:
            print(f"Error: {actual_test_example_module} file not found")