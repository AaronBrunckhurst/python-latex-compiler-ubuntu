import subprocess
import os
import sys

def is_package_installed(package_name):
    """Check if a package is installed."""
    try:
        subprocess.run(['dpkg-query', '-W', '-f=${Status}', package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_prerequisites():
    """Install necessary LaTeX packages if not already installed."""
    packages = [
        'texlive-latex-base', 'texlive-latex-recommended', 'texlive-latex-extra',
        'texlive-fonts-recommended', 'texlive-fonts-extra', 'texlive-bibtex-extra'
    ]
    
    try:
        #subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        for package in packages:
            if not is_package_installed(package):
                subprocess.run(['sudo', 'apt-get', 'install', '-y', package], check=True)
            else:
                print(f"Package {package} is already installed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing prerequisites: {e}")
        sys.exit(1)

def compile_latex(tex_file):
    """Compile a .tex file into a .pdf file."""
    if not os.path.isfile(tex_file):
        print(f"File not found: {tex_file}")
        sys.exit(1)
    
    try:
        subprocess.run(['pdflatex', tex_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while compiling the LaTeX document: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compile_latex.py <path_to_tex_file>")
        sys.exit(1)

    tex_file = sys.argv[1]

    install_prerequisites()
    compile_latex(tex_file)
    print("Compilation completed successfully.")
