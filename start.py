import subprocess
import sys
from pathlib import Path
import webbrowser

def check_sourcecode():
    # Check if sourcecode directory exists
    return (Path(__file__).parent / '.git').exists()

def check_rsk():
    # Check if RSK is installed
    try:
        import rsk
        return True
    except ImportError:
        return False

def ask_user(question):
    # Ask user for yes/no confirmation
    while True:
        response = input(f"{question} (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        if response in ['no', 'n']:
            return False
        print("Please answer 'yes' or 'no'")

def run_setup(no_rsk=False, no_clone=False):
    # Run setup.py with specific flags
    try:
        cmd = [sys.executable, 'setup.py']
        if no_rsk:
            cmd.append('--no-install')
        if no_clone:
            cmd.append('--no-clone')
        cmd.append('--no-start')  # Always skip start to avoid recursion
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Setup failed: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Error running setup: {str(e)}")
        return False

def start_processes():
    # Start the required processes
    try:
        # Start run.py in a new terminal
        run_script = Path(__file__).parent / 'run.py'
        if not run_script.exists():
            print("Error: run.py not found")
            return False
        # Start game controller
        subprocess.Popen(f'start cmd /c {sys.executable} -m rsk.game_controller -s & pause', 
                       shell=True)
        
        # Start run.py
        subprocess.Popen(f'start cmd /c {sys.executable} "{run_script}" & pause', 
                       shell=True)
        webbrowser.open('http://127.0.0.1:5000')
        
        return True
    except Exception as e:
        print(f"Error starting processes: {str(e)}")
        return False

def main():
    # Check requirements
    rsk_installed = check_rsk()
    sourcecode_exists = check_sourcecode()

    # Handle missing requirements
    if not rsk_installed or not sourcecode_exists:
        print("\nMissing requirements detected:")
        if not rsk_installed:
            print("- RSK is not installed")
        if not sourcecode_exists:
            print("- Source code is not present")
        
        if ask_user("\nWould you like to install missing components?"):
            print("\nInstalling missing components...")
            if not run_setup(no_rsk=rsk_installed, no_clone=sourcecode_exists):
                print("Failed to install requirements")
                sys.exit(1)
            # Rerun main() to check if everything is now installed
            return main()
        else:
            print("Cannot continue without required components")
            sys.exit(1)

    # Start the application
    print("\nStarting application...")
    if not start_processes():
        print("Failed to start application")
        sys.exit(1)
    
    print("\nApplication started successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()