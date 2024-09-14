# Some Scrabble Game

## How to Set Up the Python Environment

### 1. Install Python 3.10.13

If you don't have Python 3.10.13 installed, we recommend using `pyenv` to manage Python versions:

1. **Install `pyenv` (if not already installed):**
    - **macOS:** Use Homebrew:
        
        ```bash
        brew install pyenv
        ```
        
    - **Linux:** Follow the instructions [here](https://github.com/pyenv/pyenv-installer).
2. **Install Python 3.10.13 using `pyenv`:**
    
    ```bash
    pyenv install 3.10.13
    ```
    
3. **Set Python 3.10.13 as the global version**
    
    ```bash
    pyenv global 3.10.13
    ```
    

### 2. Set up the virtual environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```