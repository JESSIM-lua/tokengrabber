### README for Token Grabber Script

# Token Grabber

> **Warning:** This project is for educational purposes only. Unauthorized access to someone else's data is illegal and unethical.

## Description

This script searches for Discord tokens stored on a user's computer and displays them in the terminal. It traverses through specific directories associated with Discord and various browsers to locate the tokens.

## Features

- Searches for Discord tokens in various locations on a Windows machine.
- Outputs the found tokens to the terminal for inspection.
- Designed for educational and ethical hacking purposes.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine:

    ```sh
    git clone https://github.com/JESSIM-lua/tokengrabber.git
    ```

2. Navigate to the project directory:

    ```sh
    cd token-grabber
    ```

## Usage

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Run the script:

    ```sh
    python token_grabber.py
    ```

## How It Works

The script performs the following steps:

1. Defines the paths to search for tokens in various locations where Discord and browsers may store tokens.
2. Traverses these directories, searching for files with extensions `.log` and `.ldb`.
3. Uses regular expressions to find and extract tokens from these files.
4. Prints the found tokens to the terminal.



## License

This project is licensed under the Copyleft License.

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse of this tool. Always use ethical practices and respect others' privacy.
