# Adventure-World
A very boring text adventure game

## Usage

To use this application, follow these steps:

### Setting up a Virtual Environment

#### macOS & Linux

1. Open a terminal.

2. Navigate to your project directory.

3. Create a virtual environment:
   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```

#### Windows

1. Open a command prompt.

2. Navigate to your project directory.

3. Create a virtual environment:
   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate
   ```

### Installing Dependencies

1. While inside the activated virtual environment, install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

### Running the Application

1. Ensure your virtual environment is activated.

2. Run the application:
   ```bash
   python3 main.py
   ```

### Running Tests

1. Execute the following command to run the test suite:

    ```bash
    python -m pytest tests/
    ```

    This command uses `pytest` to run all the test files located in the `tests/` directory.
    
2. After running the tests, review the output in the terminal. Any failures or errors encountered during testing will be displayed, allowing you to troubleshoot and fix issues.

### Deactivating the Virtual Environment

When you're done using the application, deactivate the virtual environment:
```bash
deactivate
```

## License

This project is licensed under the [MIT License](LICENSE).

