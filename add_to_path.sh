#!/bin/bash

check_for_scripts_dir() {
    if [ ! -d "$HOME/scripts" ]; then
        return 1
    fi
    if [ ! -d "$HOME/scripts/sys" ]; then
        return 2
    fi

    return 0
}

# Ask the user if they want to create the scripts directory
create_directory_prompt() {
    echo "The scripts directory does not exist."
    read -p "Do you want to create it? (y/n): " create_dir

    if [[ $create_dir =~ ^[Yy]$ ]]; then
        return 0
    fi

    return 1
}

create_scripts_directory() {
    mkdir -p "$HOME/scripts/sys"
}

add_line_to_bashrc() {
    local line_to_add=$1

    echo "line_to_add: $line_to_add"

    # Check if the line is already present in .bashrc
    if ! grep -qF "$line_to_add" ~/.bashrc; then
        # If not present, add the line to the end of .bashrc
        echo "$line_to_add" >> ~/.bashrc
        echo "Line added to .bashrc"
    else
        echo "Line already exists in .bashrc. Nothing to do."
    fi
}

# Check for if the scripts directory does not exist, then create it, 0 if it exists, not 0 if it does not
check_for_scripts_dir
if [ $? -ne 0 ]; then
    create_directory_prompt
    if [ $? -eq 0 ]; then
        create_scripts_directory
        add_line_to_bashrc "export PATH=~/scripts/sys:\$PATH"
    else
        echo "User said no, making no system changes and exiting."
        exit 0
    fi
fi

# My working directory/compile_latex.py
script_path="$(pwd)/compile_latex.py"
runner_path="$HOME/scripts/compile_latex.bash"

printf "#!/bin/bash\npython3 \"%s\" \"\$1\"" "$script_path" > "$runner_path"
chmod +x "$runner_path"
ln -sf "$runner_path" "$HOME/scripts/sys/compile_latex"
