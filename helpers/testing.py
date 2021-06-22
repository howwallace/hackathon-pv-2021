'''
Used to help you test your function definitions.
Please don't modify!
'''

import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_function_output_for_input_equals_expected(function, input, output_expected,
    should_unpack_input=False, verbose=False):

    if verbose:
        print('input', input)
    output_actual = function(*input) if should_unpack_input else function(input)
    try:
        if verbose:
            print('output', output_actual)
        assert output_actual == output_expected
    except AssertionError:
        print(f' ... {bcolors.FAIL + bcolors.BOLD}failed{bcolors.ENDC}')
        print('input:    ', input)
        print('output:   ', output_actual)
        print('expected: ', output_expected)
        print()
        return False
    return True


def test_function(func, inputs, outputs, func_name_str, should_unpack_input=False, verbose=False):
    print(f'{func_name_str}')
    for (input, output) in zip(inputs, outputs):
        if not test_function_output_for_input_equals_expected(
            func, input, output, should_unpack_input=should_unpack_input, verbose=verbose
        ):
            return
    print(f' ... {bcolors.OKGREEN + bcolors.BOLD}passed all tests{bcolors.ENDC}\n')

