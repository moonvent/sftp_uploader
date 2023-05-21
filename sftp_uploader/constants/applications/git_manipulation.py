GIT_IGNORE_FILENAME = '.gitignore'


GIT_HOOK_SCRIPT_TO_UPLOAD = """
architecture=$(uname -m)

if [ "$architecture" == "x86_64" ]; then
    python main.py
elif [ "$architecture" == "arm64" ]; then
    arch -arm64 python main.py
else
    echo "Unsupported architecture: $architecture"
fi
"""


GIT_HOOKS_FOLDER = '.git/hooks/'
GIT_HOOK_PRECOMMIT_FILE = f'{GIT_HOOKS_FOLDER}pre-commit'
