"""
File: harness.py
----------------

The lab harness for CS 41 that allows the user to interact with the testable
functions in their lab assignment.

History
-------
8/9/2020 -- Created by @psarin
8/12/2020 -- Looks like we're using cmd!
"""
import cmd           # For the terminal interface
import inspect       # For grabbing information about student functions
import os            # For the files in the current dir
from typing import * # For enforcing and displaying type information
import traceback     # For displaying errors to students


def get_testable_functions():
    """
    Returns a list of the testable functions by extracting them from the Python
    files in the current directory.
    """
    # Check the files that aren't the current file.
    curr_file = os.path.basename(__file__)
    files_to_check = [
        f for f in os.listdir() if f.endswith('.py') and f != curr_file
    ]

    # Collect a list of functions to test
    output = []
    for file in files_to_check:
        module_name = file[:-3]
        module = __import__(module_name)

        try:
            output += module.TESTABLE
        except AttributeError:
            # No testable functions in the file
            pass

    return output


class Harness(cmd.Cmd):
    prompt = '🦄 > '

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = choices
        self.intro = (
            "Welcome to the CS 41 Lab Harness! Type ? or help to get a list of "
            "commands or type \na number to execute tests on that function.\n\n"
            f"Functions\n=========\n{self._make_choices_lst(choices)}\n"
        )


    @staticmethod
    def _get_signature(fn):
        """
        Returns the signature of fn as a string, where fn is a callable object.
        """
        return f"{fn.__name__}{inspect.signature(fn)}"


    @staticmethod
    def _make_choices_lst(choices):
        """
        Join function choices togeher into an indexed list
        """
        return '\n'.join([
            "{}: {}".format(i+1, Harness._get_signature(choice)) 
            for i, choice in enumerate(choices)
        ])


    def default(self, arg):
        """
        The default interpretation of arg.
        """
        try:
            chosen_i = int(arg) - 1
            chosen_f = self.choices[chosen_i]
        except ValueError:
            print("Please enter a valid command.")
            return
        except IndexError:
            print(f"Please enter a number between 1 and {len(self.choices)}.")
            return

        self.test(chosen_f)


    @staticmethod
    def _get_arg(arg_name: str, arg_type=None):
        """
        Prompts the user for an arg_name of type arg_type and returns the result
        once they enter valid Python code.
        """
        type_hint = ''
        type_comparison = None

        # Define the type hint and find the highest object we can compare to
        if arg_type:
            type_hint = f' ({arg_type})' if arg_type else ''
            try:
                type_comparison = arg_type.__origin__
            except AttributeError:
                type_comparison = arg_type

        # Combine those to the prompt
        prompt = f"{arg_name}{type_hint.replace('typing.', '')}? "

        # Prompt until the user inputs a good value
        while True:
            try:
                res = eval(input(prompt))
            except Exception as e:
                print(f"Your input raised an error: {e}. Try again.")
                continue

            if not isinstance(res, type_comparison):
                print("You didn't enter an object with the correct type.")
                continue
            
            break

        return res


    @staticmethod
    def test(fn):
        """
        Initiates tests on the function fn.
        """
        print(f"Testing {Harness._get_signature(fn)} \nPlease enter valid "
               "Python code as inputs for each of the arguments.")

        argspec = inspect.getfullargspec(fn)
        annotations = argspec.annotations

        # Collect information about what to pass to the funciton
        args = []
        for arg in argspec.args:
            args.append(Harness._get_arg(arg, annotations.get(arg)))

        varargs = ()
        if argspec.varargs:
            varargs = Harness._get_arg(argspec.varargs, tuple)

        kwonlyargs = {}
        for arg in argspec.kwonlyargs:
            kwonlyargs[arg] = Harness._get_arg(arg, annotations.get(arg))

        varkw = {}
        if argspec.varkw:
            varkw = Harness._get_arg(argspec.varkw, dict)

        # Collect the args into a string
        str_arg_lst = [str(a) for a in args + list(varargs)] \
                      + [f"{k}={repr(v)}" for k, v in kwonlyargs.items()] \
                      + [f"{k}={repr(v)}" for k, v in varkw.items()]
        str_rep = ', '.join(str_arg_lst)

        # Run the function
        print()
        print(f"Calling {fn.__name__}({str_rep})...")
        try:
            retval = fn(*args, *varargs, **kwonlyargs, **varkw)
        except Exception as e:
            print(f"The function raised an error: {e}.")
            print(traceback.format_exc(chain=False))
        else:
            print(f"Out: {repr(retval)}")
            print()


    def do_exit(self, arg):
        'Closes the CS 41 lab harness.'
        print("Good bye! Have a lovely, unicorn-filled day.")
        return True


    def do_list(self, arg):
        'Prints a list of functions that are available for testing.'
        print(f"Functions\n=========\n{self._make_choices_lst(choices)}\n")


if __name__ == '__main__':
    Harness(get_testable_functions()).cmdloop()
