# Lucas Number Series with Static Code Analysis using Pylint

This repository contains the Python script to compute the **Lucas number (Ln)** based on the given recurrence relation. The project also includes the use of **Pylint** to perform static code analysis and improve the code by addressing the recommended changes.

## Problem Description

The Lucas number series is defined as follows:
- \( L_0 = -3 \)
- \( L_1 = -1 \)
- For \( n > 1 \), the sequence follows the recurrence relation:
  \[
  L_n = L_{n-1} + L_{n-2}
  \]

The task is to write a Python script that:
1. Takes an integer `n` as input (where \( 1 < n < 1000001 \)).
2. Returns the corresponding Lucas number \( L_n \).

### Example:
- Input: `n = 2`
- Output: `L2 = -4`

The script also includes **Pylint** for static code analysis to improve code quality. After running the Pylint tool and making necessary changes, the script’s lint score is recorded.


## Script Description

### `lucasinitial.py`

This script implements the following steps:
1. **Input Handling:** Takes an integer `n` as input from the user.
2. **Lucas Number Calculation:** Uses the recurrence relation to calculate the Lucas number \( L_n \) based on the input `n`.
3. **Output:** Prints the corresponding Lucas number \( L_n \).

### Linting Process:
- **Pylint** is used to perform a static analysis of the code.
- It checks the code for potential issues such as:
  - Code formatting issues (e.g., incorrect indentation, line length).
  - Missing or unused imports.
  - Undefined variables and incorrect function calls.
  - Improper naming conventions.
  - Complexity and readability improvements.

- **Recommendations**: Based on the linting results, several recommendations for improvement may be made. These could include refactoring code, improving naming conventions, simplifying complex statements, and other best practices.
  
After addressing the recommended changes, the script is re-linted, and the updated lint score is recorded.

