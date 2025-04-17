@echo off
echo Compiling LaTeX Resume...
echo.

REM Check if pdflatex is available
where pdflatex >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Error: pdflatex not found.
    echo Please install a LaTeX distribution such as MiKTeX or TeX Live.
    echo Visit: https://miktex.org/ or https://tug.org/texlive/
    pause
    exit /b 1
)

REM Run pdflatex twice to ensure proper formatting
pdflatex resume.tex
if %ERRORLEVEL% neq 0 (
    echo Error occurred during first compilation.
    pause
    exit /b 1
)

pdflatex resume.tex
if %ERRORLEVEL% neq 0 (
    echo Error occurred during second compilation.
    pause
    exit /b 1
)

echo.
echo Resume successfully compiled to resume.pdf
echo.

REM Check if the PDF exists
if exist resume.pdf (
    echo Do you want to open the PDF now? (Y/N)
    set /p OPEN_PDF=
    if /i "%OPEN_PDF%"=="Y" (
        start resume.pdf
    )
)

echo.
echo Press any key to exit...
pause >nul 