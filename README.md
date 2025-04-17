# LaTeX CV Generator

A professional CV/resume generator built with LaTeX, designed to create polished, ATS-friendly resumes with customizable templates.

## Project Overview

This project provides a framework for creating and compiling professional CVs using LaTeX. It includes:

- Pre-configured LaTeX templates (currently English one-column design)
- Python compilation script for cross-platform support
- Windows batch file for easy compilation
- Support for LaTeX-to-PDF conversion with quality typography

For detailed information about how the project works, see [Project Pipeline](project_pipeline.md).

For step-by-step instructions on getting started, see [Getting Started Guide](getting_started.md).

## File Structure

```
latex-cv/
├── .git/                  # Git repository files
├── .gitignore             # Git ignore file
├── compile_resume.py      # Python script for compiling LaTeX to PDF
├── compile_resume.bat     # Windows batch script for compilation
├── requirements.txt       # Python dependencies information (none required)
├── README.md              # Project documentation
├── project_pipeline.md    # Detailed workflow explanation
├── getting_started.md     # Step-by-step guide for new users
├── LICENSE                # License information
└── english-oneColumn/     # English CV template (one-column layout)
    ├── resume.tex         # LaTeX source file for the CV
    └── resume.pdf         # Compiled PDF output
```

## Prerequisites

1. **LaTeX Distribution**:
   - Windows: [MiKTeX](https://miktex.org/) or [TeX Live](https://tug.org/texlive/)
   - macOS: [MacTeX](https://www.tug.org/mactex/)
   - Linux: [TeX Live](https://tug.org/texlive/)

2. **Python 3.7+** (for compilation script):
   - No additional packages required

## Quick Start

### Method 1: Using Python Script (Cross-Platform)

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/latex-cv.git
   cd latex-cv
   ```

2. Edit the appropriate template in the templates directory:
   - Open `english-oneColumn/resume.tex` in your preferred text editor
   - Modify the content to match your personal information, experience, and skills

3. Compile your resume using the Python script:
   ```
   python compile_resume.py english-oneColumn/resume.tex --open
   ```
   - This will compile the LaTeX file into a PDF and open it automatically
   - Add `--cleanup` flag to remove auxiliary files after compilation

### Method 2: Using Batch File (Windows Only)

1. Navigate to the template directory:
   ```
   cd english-oneColumn
   ```

2. Run the batch file:
   ```
   ..\compile_resume.bat
   ```
   - The batch file will compile the resume and prompt to open the PDF

### Method 3: Manual Compilation

If you prefer to use your own LaTeX workflow:

1. Navigate to the template directory:
   ```
   cd english-oneColumn
   ```

2. Run pdflatex twice to ensure proper formatting:
   ```
   pdflatex resume.tex
   pdflatex resume.tex
   ```

## Advanced Usage

### Customizing Templates

The templates are designed to be easily customizable:

1. **Structure**: Modify the sections in the LaTeX file to match your needs
2. **Styling**: Adjust colors, fonts, and spacing in the preamble
3. **Content**: Fill in your personal information, experience, and skills

### Creating New Templates

To create a new template:

1. Create a new directory for your template:
   ```
   mkdir my-custom-template
   ```

2. Copy an existing template as a starting point:
   ```
   cp english-oneColumn/resume.tex my-custom-template/
   ```

3. Customize the template to your preferences

## Troubleshooting

### Common LaTeX Errors

- **Missing Packages**: If you encounter errors about missing LaTeX packages, allow your LaTeX distribution to install them automatically
- **Compilation Errors**: Check the log file (`resume.log`) for detailed error information
- **PDF Not Generated**: Ensure you have sufficient permissions and all required LaTeX packages are installed

### Python Script Issues

- **Python Not Found**: Ensure Python is installed and in your PATH
- **Command Line Errors**: Check that you've provided the correct path to the LaTeX file

## License

This project is licensed under the terms of the license included in the repository.

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request.