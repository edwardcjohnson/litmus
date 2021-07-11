import inspect
import sys


def compose_test_module_skeleton(module_file):
    """
    Writes a pytest file based on the given module.
    Args:
        module_file (str): path to python module. e.g. "example_module.py"
    """
    module = str(inspect.getmodulename(module_file))
    test_module_file = f"test_{module}.py"

    exec(f"import {module}")
    class_members = inspect.getmembers(sys.modules[module], inspect.isclass)

    skeleton = (
"""
import pytest
"""
    )
    for class_member in class_members:
        method_members = inspect.getmembers(
            class_member[1], predicate=inspect.isfunction) # predicate=inspect.ismethod
        with open(test_module_file, "w") as f:
            for method in method_members:
                method_name = method[0]
                method_signature = inspect.signature(method[1])
                args = [arg for arg in method_signature.parameters.keys() if arg != 'self']
                if args:
                    params_dict_str = params_function_str = ""

                    for i in range(len(args)):
                        if i < len(args)-1:
                            params_dict_str_end_format = ",\n\t\t\t\t\t"
                            params_function_str_end_format = ", "
                        else:
                            params_dict_str_end_format = params_function_str_end_format = ""
                        params_dict_str += f"'{args[i]}': 3{params_dict_str_end_format}"
                        params_function_str += f"params['{args[i]}']{params_function_str_end_format}"

                    skeleton += compose_test_class_skeleton(module, class_member[0], method_name, params_dict_str, params_function_str)
            f.write(skeleton)


def compose_test_class_skeleton(module, class_member, method, params_dict_str, params_function_str):
    return (
f"""
class TestClass{method.capitalize()}():

    @pytest.mark.parametrize(
        "params,expected",
        [
            [
                {{
                    {params_dict_str}
                }},
                9
            ]
        ]
    )
    def test_return(self, params, expected):
        import tests.{module} as {module}
        assert {module}.{class_member}().{method}({params_function_str}) == expected
"""
)