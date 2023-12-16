# Adventure-World
A very boring text adventure game

## Prerequisites

Running the application on Windows requires some extra steps. First, ensure you have the Microsoft C++ Build Tools installed. These tools are necessary for compiling certain dependencies.

### Installing Microsoft C++ Build Tools

1. Visit the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) download page.
2. Download and run the installer.
3. Follow the installation instructions and make sure to include necessary C++ components.
4. Once installed, restart your system if required.

If you are on Windows and your python version is >=3.9, you will need a virtual environment with python3.8.10. This is best achieved by using pyenv in Windows Powershell. If your python version is <=3.8.10, you can skip this step. Check your python version with:
```bash
python --version
```

### Installing pyenv for Windows

#### Powershell

1. To install run:
```bash
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
If you are getting any UnauthorizedAccess error as below then start Windows PowerShell with the "Run as administrator" option and run
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
``` 
Now re-run the above installation command.

2. Close and re-open powershell.

3. Verify the installation was successfull with:
```bash
pyenv --version
```
You should see the version number printed to the console. If the command is not recognised, follow hese instruction to verify your environment variables https://github.com/pyenv-win/pyenv-win/blob/master/README.md#manually-check-the-settings

4. Install python3.8 with:
```bash
pyenv install 3.8.10
```

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
 This assumes the above prerequisites completed successfully.

1. Open Windows Powershell.

2. Navigate to your project directory.

3. If your python version is >=3.9, set your local version with pyenv:

```bash
pyenv local 3.8.10
```

4. Create a virtual environment:
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

