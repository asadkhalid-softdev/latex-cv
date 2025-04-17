# Getting Started with LaTeX CV Generator

This guide will help you get up and running with the LaTeX CV Generator quickly.

## Initial Setup

### Step 1: Install LaTeX

The LaTeX CV Generator requires a LaTeX distribution to compile your resume/CV.

**For Windows:**
1. Download and install [MiKTeX](https://miktex.org/download) or [TeX Live](https://tug.org/texlive/acquire-netinstall.html)
2. During installation, choose to install missing packages automatically when needed

**For macOS:**
1. Download and install [MacTeX](https://www.tug.org/mactex/mactex-download.html)
2. This includes the full TeX Live distribution and additional tools

**For Linux:**
1. Install TeX Live using your package manager:
   ```bash
   # For Ubuntu/Debian
   sudo apt-get install texlive-full
   
   # For Fedora
   sudo dnf install texlive-scheme-full
   
   # For Arch Linux
   sudo pacman -S texlive-most
   ```

### Step 2: Install Python (for compilation script)

1. Download and install [Python 3.7+](https://www.python.org/downloads/) if not already installed
2. Verify installation by running:
   ```bash
   python --version
   ```

### Step 3: Clone the Repository

```bash
git clone https://github.com/yourusername/latex-cv.git
cd latex-cv
```

### Step 4: Verify Python Script

No additional Python packages are required as the compilation script uses only standard libraries.

## Creating Your First CV/Resume

### Step 1: Choose a Template

The project currently includes an English one-column template:
- `english-oneColumn/resume.tex`

### Step 2: Edit the Template

1. Open `english-oneColumn/resume.tex` in your favorite text editor
2. Modify the personal information section:
   ```latex
   \begin{center}
       \textbf{\fontsize{24}{28}\selectfont\scshape Your Name} \\ \vspace{12pt}
       \small
       Phone: +1234567890 \quad
       Email: your.email@example.com \\ \vspace{4pt}
       \href{https://www.linkedin.com/in/yourprofile/}{linkedin.com/in/yourprofile} \quad
       \href{https://github.com/yourusername}{github.com/yourusername} \\ \vspace{4pt}
       Address: Your City, Country
   \end{center}
   ```

3. Update each section with your information:
   - Professional Summary
   - Skills
   - Languages
   - Experience
   - Education
   - Publications (if applicable)

### Step 3: Compile Your Resume

#### Using Python Script (Recommended)

```bash
python compile_resume.py english-oneColumn/resume.tex --open
```

This will:
1. Compile your LaTeX file into a PDF
2. Open the PDF automatically for review
3. To also clean up auxiliary files, add the `--cleanup` flag:
   ```bash
   python compile_resume.py english-oneColumn/resume.tex --open --cleanup
   ```

#### Using Batch File (Windows Only)

1. Navigate to your template directory:
   ```bash
   cd english-oneColumn
   ```

2. Run the batch file:
   ```bash
   ..\compile_resume.bat
   ```

3. When prompted, press Y to open the PDF

### Step 4: Review and Iterate

1. Review your PDF for any formatting issues or content adjustments
2. Return to the `.tex` file to make any necessary changes
3. Recompile to see your updates

## Customization Tips

### Adjusting Section Order

Sections in the template can be reordered by moving their corresponding LaTeX code blocks. For example, to move Education before Experience, cut the entire Education section and paste it before the Experience section.

### Modifying Fonts and Colors

In the preamble section (top of the file), you can adjust:

1. **Font size**:
   ```latex
   \documentclass[letterpaper,11pt]{article}  % Change 11pt to adjust overall font size
   ```

2. **Section colors**:
   ```latex
   \definecolor{sectionColor}{RGB}{70,70,70}  % Change RGB values for different colors
   ```

3. **Typography**:
   The template uses sans-serif fonts by default for better on-screen readability and ATS compatibility:
   ```latex
   \renewcommand{\familydefault}{\sfdefault}  % Set default font to sans-serif
   ```

### Adding or Removing Sections

To add a new section:

```latex
\section{NEW SECTION NAME}
% Your section content here
```

## Troubleshooting

### Common Issues

1. **"LaTeX Error: File 'xcolor.sty' not found"**
   - Solution: Install the missing package via your LaTeX distribution
   - For MiKTeX, it will prompt to install automatically
   - For TeX Live, run: `tlmgr install xcolor`

2. **PDF Not Opening Automatically**
   - Solution: Open the PDF manually from the template directory
   - Check for any errors in the terminal output

3. **Formatting Issues**
   - Solution: Ensure you compile twice (the script does this automatically)
   - Check the `.log` file for warnings or errors

### Getting Help

If you encounter issues not covered in this guide:

1. Check the LaTeX documentation for specific packages
2. Search for LaTeX errors online
3. Open an issue in the project repository with details about your problem 