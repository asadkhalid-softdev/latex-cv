#!/usr/bin/env python
"""
Script to compile the LaTeX resume and verify the generated PDF.
"""
import os
import subprocess
import sys
import platform
import shutil
import argparse

def compile_latex_resume(tex_file):
    """Compile the LaTeX resume file into a PDF."""
    print(f"Compiling {tex_file}...")
    
    # Check if pdflatex is installed
    pdflatex_path = shutil.which("pdflatex")
    if not pdflatex_path:
        print("Error: pdflatex not found. Please install a LaTeX distribution:")
        print("  - Windows: MiKTeX or TeX Live")
        print("  - macOS: MacTeX")
        print("  - Linux: TeX Live")
        return False
    
    # Run pdflatex twice to ensure proper formatting and references
    for i in range(2):
        result = subprocess.run(
            ["pdflatex", tex_file],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(tex_file))
        )
        
        if result.returncode != 0:
            print(f"Error compiling LaTeX file: {result.stderr}")
            return False
    
    pdf_file = os.path.splitext(tex_file)[0] + ".pdf"
    
    if os.path.exists(pdf_file):
        print(f"✓ Successfully compiled {pdf_file}")
        print(f"  PDF Size: {os.path.getsize(pdf_file) / 1024:.1f} KB")
        return True
    else:
        print(f"Error: PDF file {pdf_file} was not created")
        return False

def cleanup_auxiliary_files(base_name):
    """Remove auxiliary files generated during LaTeX compilation."""
    extensions = ['.aux', '.log', '.out', '.toc']
    for ext in extensions:
        aux_file = base_name + ext
        if os.path.exists(aux_file):
            try:
                os.remove(aux_file)
                print(f"Removed auxiliary file: {aux_file}")
            except OSError as e:
                print(f"Error removing {aux_file}: {e}")

def open_pdf(pdf_file):
    """Attempt to open the generated PDF file."""
    if not os.path.exists(pdf_file):
        return
    
    system = platform.system()
    try:
        if system == 'Windows':
            os.startfile(pdf_file)
        elif system == 'Darwin':  # macOS
            subprocess.run(['open', pdf_file])
        else:  # Linux and other Unix-like
            subprocess.run(['xdg-open', pdf_file])
        print(f"Opened {pdf_file}")
    except Exception as e:
        print(f"Could not open PDF automatically: {e}")
        print(f"Please open {pdf_file} manually")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Compile a LaTeX resume file into a PDF.')
    parser.add_argument('tex_file', nargs='?', 
                      help='Path to the LaTeX resume file')
    parser.add_argument('--cleanup', action='store_true',
                      help='Clean up auxiliary files after compilation')
    parser.add_argument('--open', action='store_true',
                      help='Open the PDF after compilation')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    # Use provided path or default to resume.tex in script directory
    if args.tex_file:
        tex_file = os.path.abspath(args.tex_file)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tex_file = os.path.join(script_dir, "resume.tex")
    
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} not found!")
        sys.exit(1)
    
    if compile_latex_resume(tex_file):
        base_name = os.path.splitext(tex_file)[0]
        pdf_file = base_name + ".pdf"
        
        if args.cleanup:
            cleanup_auxiliary_files(base_name)
        
        print(f"\nResume PDF created: {pdf_file}")
        print("You can now use this PDF for job applications.")
        
        if args.open:
            open_pdf(pdf_file) 