# IPv4 Address Validator

This repository contains a Python script that validates IPv4 addresses using regular expressions (Regex). It also includes a set of pytest tests to ensure that the validator behaves as expected.

---

## Features

- **IPv4 Address Validation:**  
  The script checks if a given string is a valid IPv4 address. An address is considered valid if it consists of four octets separated by dots, with each octet being a number between 0 and 255.

- **Regex-Based Implementation:**  
  The validation logic is implemented using a concise and efficient regular expression that matches the criteria for IPv4 addresses.

- **Automated Testing:**  
  The repository includes tests written with [pytest](https://docs.pytest.org/) to verify the correctness of the IPv4 address validation function. This helps maintain code quality and ensures that changes do not break the intended functionality.

---

## Files

- **IPv4_Address.py**  
  This file contains the main implementation of the IPv4 validation function and the script’s entry point. It reads an IPv4 address from user input and prints whether the address is valid (`True`) or not (`False`).

- **test_ipv4_address.py**  
  This file contains a series of pytest tests. The tests are designed to cover:
  - **Loopback Addresses:** e.g., "127.0.0.1" and "127.0.0.0"
  - **Modem/Private Addresses:** e.g., "192.168.6.1" and "192.168.90.1"
  - **Incorrect Addresses:** e.g., "10.10.10.10.10", "256.0.0.1", and "254.0.765.1"

---

## Getting Started

### Prerequisites

- **Python 3.x:** Make sure you have Python 3 installed.
- **pytest:** Install pytest for running tests. You can install it using pip:

  ```bash
  pip install pytest
  ```

### Running the Script

To run the IPv4 address validator, execute the following command in your terminal:

```bash
python IPv4_Address.py
```

You will be prompted to enter an IPv4 address. The script will output `True` if the address is valid and `False` otherwise.

### Running the Tests

To run the automated tests, simply run:

```bash
pytest test_ipv4_address.py
```

pytest will discover the tests and display the results, ensuring that all cases pass as expected.

---

## Code Overview

### IPv4_Address.py

- **validate(ip: str) -> bool:**  
  This function uses a regular expression to check whether the input string is a valid IPv4 address. The regex ensures:
  - There are exactly four numeric segments.
  - Each segment is between 0 and 255.
  
- **main():**  
  The main function that prompts the user for an IPv4 address, calls the validation function, and prints the result.

### test_ipv4_address.py

- **Test Functions:**  
  The tests include:
  - `test_LoopBack()`: Verifies loopback addresses.
  - `test_ModemAddress()`: Checks typical private IP addresses.
  - `test_WrongAddress()`: Confirms that improperly formatted or out-of-range addresses return `False`.

---

## Contributing

Feel free to fork this repository and submit pull requests if you have suggestions or improvements. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgements

- Special thanks to the developers and contributors who maintain and improve the Python ecosystem and tools like pytest.
