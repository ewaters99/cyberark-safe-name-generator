# cyberark-safe-name-generator
CyberArk Safe Name Generator - based on safe naming convention best practices.

## Description

The Safe Name Generator is a Python-based tool designed to create safe names according to the CyberArk Safe Naming convention best practices. It helps in generating structured and meaningful names by prompting the user to select options from predefined categories such as Environment, Business Unit, Technology, Operating System, and Account Type.

## Features

- **Customizable Naming Convention:** Supports a variety of categories to fit different organizational needs.
- **Compliance with Naming Restrictions:** Ensures generated names do not exceed 28 characters, aligning with best practices.
- **User-Friendly Interface:** Offers a simple CLI interface for easy interaction and selection.
- **Support for Least Privilege Concept:** Facilitates the creation of segregated access controls by providing distinct and meaningful safe names.

## Installation

1. **Prerequisites:**
   - Python 3.6 or later
   - `termcolor` package

2. **Setup:**
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ewaters99/cyberark-safe-name-generator.git
   ```

3. **Install Dependencies:**

   Navigate to the project directory and install the required packages:

   ```bash
   cd safe-name-generator
   pip install -r requirements.txt
   ```

## Usage

To run the Safe Name Generator, execute the following command in the project directory:

```bash
python safe_name_generator.py
```

Follow the on-screen prompts to select options for each category. The tool will generate a safe name based on your selections.

## Contributing

We welcome contributions to the Safe Name Generator! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Eric W. Waters** - *Initial work*

## Acknowledgments

- Thanks to the CyberArk PAM community for the inspiration behind this project.
