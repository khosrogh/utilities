import inspect
import sys

# Get all members (objects) in the current frame's global namespace
members = inspect.getmembers(inspect.currentframe().f_globals)

# Create a copy of the dictionary keys
module_names = list(sys.modules.keys())

# Include functions from imported modules, handling ImportError
for module_name in module_names:
    try:
        module = __import__(module_name)
        members.extend(inspect.getmembers(module, inspect.isfunction))
    except ImportError as e:
        print(f"Error importing module '{module_name}': {e}")

# Get the current module
current_module = sys.modules[__name__]

# Filter out Python built-in functions and modules
user_defined_functions = [
    (name, func)
    for name, func in members
    if inspect.isfunction(func) and inspect.getmodule(func) == current_module
]

# Print the names of all user-defined functions
for function_name, function_object in user_defined_functions:
    print(f"User-defined Function Name: {function_name}")
