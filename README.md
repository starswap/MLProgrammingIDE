# μλ Programming IDE
<img src="Tutorial/mainWindow.png" />
Python Programming IDE for Computer Science A Level NEA project, using artificial intelligence.
More information available on the <a href="https://htmlpreview.github.io/?https://github.com/starswap/MLProgrammingIDE/blob/main/Tutorial/tutorial.html">tutorial page</a>.

The report for this project is available <a href="https://drive.google.com/file/d/1dQ3htcXWOJ9TJyVygopYAYWSbQifKinz/view?usp=sharing">here</a>.


## Project Structure - Important Files
- **MLIDE.py** - The "main" source code file for the project - this is the file which imports all of the others.
- **MLIDE.exe** - The final IDE for deployment, as a Windows exe. Compile your own with pyinstaller. 
- **pyinstallerCommand** - Compilation command to build MLIDE.py into MLIDE.exe - don't strictly need to do this to use the IDE.
- **Syntax_Rules.txt** - The regex-specified syntax patterns which should trigger a corresponding message in the IDE when they are typed.
- **CodeFeatures.py** - Syntax Highlighting; Line Numbers; Auto-Indent; Format Code; Code Autocomplete
- **ui files** - XML source files in PyQt representing the designs for each of the screens, compiled to Python before use.   
- **npy files** - ML Weights as numpy binary.
- **FILES_TO_DISTRIBUTE** - A list of the files that need to be distributed with, and kept in the same folder as, the executable once generated.
- **MachineLearning**
  - **autocomplete.py** - RNN model to suggest completions
  - **comments.py** - "Autocomment" functionality, limited to algorithm identification for the moment.
  - **readability.py** - Generates readability scores 
  - **userProficiency.py** - Generate user's proficiency level e.g. Veteran / Student etc based on G4G article levelling.
- **Objects**
  - **HexagonObject.py** - The class definitions for each of the different types of hexagons, including their methods to update scores
  - **ProjectObject.py** - Class definition for the Project Object, including open, new, save, switch to file, execute, runFile modules
  - **UnitTestObject.py** - the UnitTest object for storing unit test data. executeTests and generateMockInput (for complexity scoring)
 - **Tutorial** - Icons and HTML file for the tutorial (help page), which opens with F12
- **UI** - Compiled Python representations of most of the UI files for the project. These are imported when they need to be displayed.
- **build** - Directory generated by PyInstaller when producing the final executable.
