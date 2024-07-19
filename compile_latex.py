import subprocess
import os
import sys

def install_prerequisites():
    """Install necessary LaTeX packages."""
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'texlive-latex-base', 'texlive-latex-recommended', 'texlive-latex-extra', 'texlive-fonts-recommended', 'texlive-fonts-extra', 'texlive-bibtex-extra'], check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing prerequisites: {}".format(e))
        sys.exit(1)

def compile_latex(tex_file):
    """Compile a .tex file into a .pdf file."""
    if not os.path.isfile(tex_file):
        print("File not found: {}".format(tex_file))
        sys.exit(1)
    
    try:
        subprocess.run(['pdflatex', tex_file], check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while compiling the LaTeX document: {}".format(e))
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compile_latex.py <path_to_tex_file>")
        sys.exit(1)

    tex_file = sys.argv[1]

    install_prerequisites()
    compile_latex(tex_file)
    print("Compilation completed successfully.")
