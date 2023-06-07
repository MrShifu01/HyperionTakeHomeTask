# Say The Name

This repository contains a Python script that converts a given number into its spoken representation. It also includes unit tests to verify the correctness of the implementation. The solution is compatible with Linux, macOS, and Windows operating systems.

---
## Dependencies

The solution requires Python 3 to be installed on the system. If you don't have it installed, you can download it from the official Python website: https://www.python.org/downloads/

---
## Usage

To convert a number into its spoken representation, you can use the `sayNumber()` function from the `sayTheNumber` module. The function takes an integer as input and returns the spoken representation as a string.

Here's an example usage:

```python
from sayTheNumber import sayNumber

number = 12345
spoken_number = sayNumber(number)

print(spoken_number)  # Output: "twelve thousand, three hundred and forty-five"
```
---
## Testing

Unit tests are provided to ensure the correctness of the `sayNumber()` function. To run the tests, follow these steps:

1. Make sure you have Python 3 installed on your system.

2. Open a terminal or command prompt and navigate to the directory containing the `test.py` file.

3. Run the following command:

   ```bash
   python test.py
   ```

   The tests will be executed, and the results will be displayed in the terminal.
---
## Containerization with Docker

If you prefer to run the solution in a Docker container, you can use the provided Dockerfile.

### Setup and Usage

1. Make sure you have Docker installed on your machine. You can download and install Docker from the official website: https://www.docker.com/get-started

2. Clone or download the repository to your local machine.

3. Open a terminal or command prompt and navigate to the project's root directory.

4. Build the Docker image by running the following command:

   ```bash
   docker build -t say-the-number .
   ```

   This will build the Docker image based on the Dockerfile in the current directory.

5. Once the image is successfully built, you can run a container based on that image using the following command:

   ```bash
   docker run say-the-number
   ```

   This will create and run a container from the `say-the-number` image, and the unit tests specified in the Dockerfile's CMD instruction will be executed within the container.

   Note: Ensure that you are in the same directory as the Dockerfile when running the `docker build` command.
---
## Worst-Case Space Complexity

The worst-case space complexity of the `sayNumber()` function is O(n), where n is the number of digits in the input number. This space complexity arises due to the recursive nature of the function.

When the function is called with a number of length n, it makes recursive calls with a smaller number (e.g., hundreds, thousands, etc.) until it reaches the base case (single-digit numbers). At each level of recursion, a new set of variables (e.g., `numberStr`, `length`, `num1`, `num2`) is created, consuming additional space.

In the worst case, when the input number has n digits, the function will make recursive calls for each group of three digits (e.g., thousands, millions, billions). Therefore, the maximum depth of recursion will be n/3, resulting in a space complexity of O(n/3). However, when simplifying the space complexity notation, we drop the constant factor, leading to a worst-case space complexity of O(n).

Please note that the worst-case space complexity is an approximation and assumes that the recursive calls are made

 for every group of three digits. In practice, the actual space usage may vary depending on the input number and its distribution of digits.

---