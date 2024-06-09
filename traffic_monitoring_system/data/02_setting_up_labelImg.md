# Setting up LabelImg in VSCode

A step-by-step guide for installing and running LabelImg using `pip`, including how to do it within Visual Studio Code (VSCode).

### Step 1: Install Python and pip

Ensure you have Python and `pip` installed on your system. You can download Python from [python.org](https://www.python.org/downloads/) if you don't have it installed.

To check if Python and `pip` are installed, run the following commands in your terminal:

```sh
python --version
pip --version
```

### Step 2: Open VSCode

1. **Open Visual Studio Code (VSCode)**.
2. **Open a Terminal in VSCode**:
   - Go to the menu and select `Terminal > New Terminal` or press ``Ctrl + ` ``.

### Step 3: Create and Activate a Virtual Environment (If Notr yet Created)

It's a good practice to create a virtual environment to manage your project's dependencies.

1. **Create a virtual environment**:
   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On **Windows**:
     ```sh
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```

### Step 4: Install LabelImg Using pip

1. **Install LabelImg**:
   ```sh
   pip install labelImg
   ```

### Step 5: Run LabelImg

After the installation is complete, you can run LabelImg directly from the terminal.

#### Ensure distutils is Installed
    For Windows, Open a Command Prompt or PowerShell as Administrator.
    ```sh
    Copy code
    python -m pip install setuptools
    ```

    For macOS/Linux:
    Open a Terminal, Run the following command:

    ```sh
    Copy code
    sudo apt-get install python3-distutils
    ```
    If you’re using pip to manage your Python packages, you might also want to install setuptools:

    ```sh
    python3 -m pip install setuptools
    ```
    **--Verify Installation**

      To verify that distutils is installed correctly, you can try importing it in a Python shell:

      ```sh
      python
      ```

      ```sh
      import distutils.spawn
      ```
      
      If there is no error, then distutils is installed correctly.
    
1. **Run LabelImg**:
   ```sh
   labelImg
   ```

This will launch the LabelImg GUI.

### Step 6: Configure LabelImg (First-Time Setup)

When you run LabelImg for the first time, you might need to set the default save directory and label directory:

1. **Set Default Save Directory**:
   - In the LabelImg GUI, go to `File > Open Dir`.
   - Select the directory containing your images.

2. **Set Default Label Directory**:
   - In the LabelImg GUI, go to `Sidebar > Change Default Save Dir`.
   - Select the directory where you want to save the annotations.

### Optional: Creating a VSCode Task for Running LabelImg

For convenience, you can create a task in VSCode to run LabelImg with a single command.

1. **Create a Task**:
   - Go to `Terminal > Configure Tasks...`.
   - Select `Create tasks.json file from template` if prompted.

2. **Edit `tasks.json`**:

   If the `tasks.json` file doesn't exist, create it manually in the `.vscode` directory of your project.

   ```json
   {
       "version": "2.0.0",
       "tasks": [
           {
               "label": "Run LabelImg",
               "type": "shell",
               "command": "labelImg",
               "group": {
                   "kind": "build",
                   "isDefault": true
               },
               "presentation": {
                   "echo": true,
                   "reveal": "always",
                   "focus": false,
                   "panel": "shared"
               },
               "problemMatcher": []
           }
       ]
   }
   ```

3. **Run the Task**:
   - Go to `Terminal > Run Task...`.
   - Select `Run LabelImg`.

### You have succesful set up LabelImg, now let head over top model training

Following these steps, you should be able to install and run LabelImg using `pip` within VSCode. 
