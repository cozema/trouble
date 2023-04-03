import subprocess

# Run Black to format the code
black_cmd = "black . --check"
black_result = subprocess.run(black_cmd, shell=True, capture_output=True, text=True)

if black_result.returncode != 0:
    print("Error: Code formatting is not correct!")
    print(black_result.stderr)
else:
    print("Code formatting is correct!")

# Run Pylint to lint the code
pylint_cmd = "pylint . --fail-under=9.5"
pylint_result = subprocess.run(pylint_cmd, shell=True, capture_output=True, text=True)

if pylint_result.returncode != 0:
    print("Error: Code linting failed!")
    print(pylint_result.stderr)
else:
    print("Code linting passed!")
