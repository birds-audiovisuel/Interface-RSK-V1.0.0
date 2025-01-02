
import subprocess
import sys
import argparse
from pathlib import Path
# Default repository URL
repo = "https://github.com/birds-audiovisuel/Interface-RSK-V1.0.0.git"

def parse_arguments():
    # Getting Arguments and return them
    parser = argparse.ArgumentParser(description='Setup RSK environment')
    parser.add_argument('--no-clone', action='store_true', help='Skip repository cloning')
    parser.add_argument('--no-install', action='store_true', help='Skip RSK installation')
    parser.add_argument('--no-start', action='store_true', help='Skip starting the application')
    parser.add_argument('--repo', default=repo, help='Repository URL to clone')
    return parser.parse_args()

# Return false if an error occurs
def clone_repository():
    # Clone the repository in the same folder as the setup.py file
    repo_path = Path(__file__).parent
    try:
        # If the repository already exists, pull the latest changes
        if not (repo_path / '.git').exists():
            print("Cloning repository...")
            result = subprocess.run(['git', 'init'],
                                 cwd=repo_path, capture_output=True, text=True)
            if result.returncode != 0:
                # Manage error
                print(f"Error initializing repository: {result.stderr}")
                return False
            result = subprocess.run(['git', 'remote','add','origin', 'https://github.com/birds-audiovisuel/Interface-RSK-V1.0.0.git'],
                                 cwd=repo_path, capture_output=True, text=True)
            if result.returncode != 0:
                # Manage error
                print(f"Error during remote repository: {result.stderr}")
                return False
            result = subprocess.run(['git', 'fetch', 'origin'],
                                 cwd=repo_path, capture_output=True, text=True)
            if result.returncode != 0:
                # Manage error
                print(f"Error fetching repository: {result.stderr}")
                return False
            result = subprocess.run(['git', 'checkout', '-b', 'main'],
                                 cwd=repo_path, capture_output=True, text=True)
            if result.returncode != 0:
                # Manage error
                print(f"Error creating main branch: {result.stderr}")
                return False
            result = subprocess.run(['git', 'pull', 'origin', 'main', '--allow-unrelated-histories'],
                                    cwd=repo_path, capture_output=True, text=True)
            if result.returncode != 0:
                # Manage error
                print(f"Error pulling repository: {result.stderr}")
                return False
            print("Repository cloned successfully.")
        else:
            # Add repository to safe.directory
            result = subprocess.run(['git', 'config', '--global', '--add', 'safe.directory', repo_path.resolve().as_posix()], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error configuring safe directory: {result.stderr}")
                return False
            print("Repository already exists, pulling latest changes...")
            result = subprocess.run(['git', 'branch', '--set-upstream-to=origin/main', 'main'], cwd=repo_path, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error setting upstream branch: {result.stderr}")
                return False
            result = subprocess.run(['git', 'pull'], cwd=repo_path, capture_output=True, text=True)
            if result.returncode != 0:
                # Manage error
                print(f"Error updating repository: {result.stderr}")
                return False
            print("Repository updated successfully.")
        return True
    except Exception as e:
        print(f"Error during repository operations: {str(e)}")
        return False

# Return false if an error occurs
def install_rsk():
    try:
        print("Installing RSK...")
        python_exe = sys.executable # Use the same Python executable that is running this script
        result = subprocess.run([python_exe, '-m', 'pip', 'install', 'robot-soccer-kit[gc]'],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error installing RSK: {result.stderr}")
            return False
        print("RSK successfully installed.")
        return True
    except Exception as e:
        print(f"Error during RSK installation: {str(e)}")
        return False

def start_application():
    try:
        print("Starting application...")
        start_script = Path(__file__).parent / 'start.py'
        if not start_script.exists():
            print("Error: start.py not found")
            return False
        subprocess.Popen([sys.executable, str(start_script)])
        return True
    except Exception as e:
        print(f"Error starting application: {str(e)}")
        return False

def main():
    args = parse_arguments()
    if args.repo:
        global repo
        repo = args.repo
    if not args.no_clone:
        if not clone_repository():
            sys.exit(1)
    if not args.no_install:
        if not install_rsk():
            sys.exit(1)
    if not args.no_start:
        if not start_application():
            sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()