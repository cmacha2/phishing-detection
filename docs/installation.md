
# Installation Guide

Follow these steps to install the Phishing Detection Framework:

## Requirements

- Python 3.8+
- pip 21.0+

## Installation

### From PyPI
```bash
pip install phishing-detection
```

### From Source
1. Clone the repository:
    ```bash
    git clone https://github.com/cmacha2/phishing-detection.git
    ```
2. Navigate to the project directory:
    ```bash
    cd phishing-detection
    ```
3. Install the library:
    ```bash
    pip install -e .
    ```

## Dependencies

This library automatically installs:
- `transformers`
- `torch`
- `scikit-learn`
- `pandas`
- `numpy`

Make sure to install `pytest` for running the test suite.

For detailed usage examples, check the [Usage Guide](usage.md).
