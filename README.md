# Programs used in "Diverse change of chemical structures from reverse string operations on SMILES notation"

## Article Information
***
This article has been submitted for publication.
***
## About this repository
***
This repository provides python codes of **ASCII Text Based Chemical Structure Tuner (ACST): String Reversal Mechanism for SMILES Notation**. There are total twelve python script and a User_Manual.pdf.

* The User_Manual.pdf provides the following details:
    * Author and Date of Documentation
    * Audience
    * Content
    * Introduction to the ACST
    * Installation Instructions
    * Description of Home Page
    * Description of Panel 1: Chemical File Translator (CFT)
    * Description and User Instruction for Panel 2: Logical Processor (LP)
    * Examples
    * Troubleshoot Problems
***
## Installation
***
### Pre-installation Requirements
* **Hardware Requirements**
    * Processor : Core i3 and above
    * RAM : minimum 2GB
    * Hard Disk : 0.5 GB (for ACST only)
    * Display : 1366 X 768
* **Software Requirments**
    * System Software : Windows 10 and above
    * Python : Version 3.11 and above
    * Tkinter : Version 8.6 and above
* **External Software Requirements**
    * Molecule Structure Drawing Software : PerkinElmer's ChemDraw [1], ACD Labs ChemSketch [2], or Avogadro software [3].
    * File Translation Software : OpenBabel [4]
    * Text Editing Software : Notepad++ [5]

### Installation Procedure
**Download:**
The source code of the software device ACST is available on the GitHub link http://github.com/paulat0grant/ACST. The source code can be cloned via download ZIP format. 

**Installation:**
Unzip the GitHub cloned ZIP file of ACST source code. Then edit the following files:

**_DrawMolecule.py_**

Edit line 2 written as:
```
subprocess.Popen(‘path of the installation directory/Avogadro.exe')
```
to the installation path like
```
subprocess.Popen(‘I:/avogadro/Install/bin/Avogadro.exe')
```

**_FileTranslate.py_**

Edit the line 6 written as:
```
subprocess.Popen(‘path of the installation directory/obgui.exe')
```
to the installation path like
```
subprocess.Popen(‘I:/openbabel/install/obgui.exe.exe')
```

**_TextEditor.py_**

Edit line 2 written as:
```
subprocess.Popen(‘path of the installation directory/notepad++.exe')
```
to the installation path like
```
subprocess.Popen('I:/notepadpp/install/notepad++.exe')
```

**Launch ACST:**

Double-click setup.py of unzipped ACST source code. 
***
## Author
Anup Paul
paulat0grant@rediffmail.com
***
## References
[1] Elmer, P., ChemBioDraw Ultra Version (14.0). CambridgeSoft Waltham, MA, USA, 2014.

[2] Acd/Labs, Acd/chemsketch (freeware), version 12.01. 2009, Canada Advanced Chemistry Developement, Inc.: Canada Toronto.­

[3] Hanwell, M.D., et al., Avogadro: an advanced semantic chemical editor, visualization, and analysis platform. Journal of cheminformatics, 2012. 4(1): p. 1-17, DOI: https://doi.org/10.1186/1758-2946-4-17.

[4] O'Boyle, N.M., et al., Open Babel: An open chemical toolbox. Journal of cheminformatics, 2011. 3(1): p. 1-14, DOI: https://doi.org/10.1186/1758-2946-3-33.

[5] Ho, D., Notepad++. Notepad Plus Plus,[Online]. Available: https://notepad-plus-plus. org/.[Accessed 7 8 2020], 2011.
