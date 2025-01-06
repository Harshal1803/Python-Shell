import sys
import os
import shutil
import readline
import subprocess
import time

RED = "\033[31m"  
GREEN = "\033[32m"  
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def print_banner():
    bold = "\033[1m"  
    banner = f"""
{GREEN}{bold}   
  
   _____              __         _____   _____     _______         _______       
  |_   _|            /  \        |_   _||_   _|   |_   __ \       |_   ___ `.     
    | |             / /\ \         | | /\ | |       | |__) |        | |   `. \    
    | |   _        / ____ \        | |/  \| |       |  __ /         | |    | |    
   _| |__/ |     _/ /    \ \_      |   /\   |      _| |  \ \_      _| |___.' /       
  |________|    |____|  |____|     |__/  \__|     |____| |___|    |________.'   

                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀        
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀    
                    ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠾⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
                    ⠀⠀⠀⣤⡄⢀⣴⠆⠀⠀⠀⢀⣤⢤⡄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
                    ⠀⠀⢸⣿⠁⣼⡟⠀⠀⠀⠀⠸⣧⣼⠏⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
                    ⠀⠀⢸⡏⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
                    ⠀⠀⣼⠁⣿⠇⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀ 
                    ⠀⠀⠈⠐⠛⢀⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠀⠀
                    ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⣉⣠⠤⠖⠀⠀⠀⠀   
                    ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠋⣉⣠⡤⠶⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⣿⡿⠿⠟⠛⢉⣁⣤⡴⠶⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   
                    ⠀⠀⠀⠀⠀⠒⠒⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        
{YELLOW}______________________________________________________________________________{RESET}
    """
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.002)  # Simulate typing effect
    sys.stdout.write("\n")
    
print_banner()    
print(f"{YELLOW}lawrd shell {RESET}\ncompletely developed in {BLUE}python{RESET}")


builtin_cmd = ["echo", "exit", "type", "pwd","ls","clear","cd","touch","rm","mkdir","exit","systeminfo"]
def completer(text, state):
    """
    Tab completion logic. Suggests commands, file paths, or directories.
    """
    
    options = builtin_cmd + os.listdir(".")
    matches = [option for option in options if option.startswith(text)]
    return matches[state] if state < len(matches) else None


def git_add(files):
    try:
        result = subprocess.run(['git', 'add'] + files, capture_output=True, text=True)
        if result.stderr:
            print(f"Error: {result.stderr}")
        else:
            print(result.stdout or "Files added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def git_push(remote="origin", branch="main"):
    try:
        result = subprocess.run(['git', 'push', remote, branch], capture_output=True, text=True)
        if result.stderr:
            print(f"Error: {result.stderr}")
        else:
            print(result.stdout or "Pushed to remote successfully.")
    except Exception as e:
        print(f"Error: {e}")

def git_clone(repo_url):
    try:
        result = subprocess.run(['git', 'clone', repo_url], capture_output=True, text=True)
        if result.stderr:
            print(f"Error: {result.stderr}")
        else:
            print(result.stdout or "Repository cloned successfully.")
    except Exception as e:
        print(f"Error: {e}")

def git_pull(remote="origin", branch="main"):
    try:
        result = subprocess.run(['git', 'pull', remote, branch], capture_output=True, text=True)
        if result.stderr:
            print(f"Error: {result.stderr}")
        else:
            print(result.stdout or "Pulled from remote successfully.")
    except Exception as e:
        print(f"Error: {e}")

def git_init():
    try:
        result = subprocess.run(['git', 'init'], capture_output=True, text=True)
        if result.stderr:
            print(f"Error: {result.stderr}")
        else:
            print(result.stdout or "Git repository initialized.")
    except Exception as e:
        print(f"Error: {e}")
                

def main():
    #builtin_cmd = ["echo", "exit", "type", "pwd"]
    PATH = os.environ.get("PATH")
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)

    commands = {
        "help": "Show this help menu with a list of available commands.",
        "pwd": "Print the current working directory.",
        "cd <dir>": "Change the current directory to <dir>. Use 'cd ~' to go to the home directory.",
        "mkdir <dir>": "Create a new directory named <dir>.",
        "rm <file/dir>": "Remove a file or directory.",
        "echo <text>": "Print the provided text to the terminal.",
        "ls": "List all files and directories in the current directory.",
        "clear": "Clear the terminal screen.",
        "exit": "Exit the shell.",
        "systeminfo": "Display system information.",
    }

    while True:
        sys.stdout.write("\033[33m" + os.getcwd() +" $>"+ "\033[30m")
        # sys.stdout.write(" $> ")
        sys.stdout.flush()
    # Wait for user input
    #input()
        #command=input()
        if command := input().strip():

            if command.startswith("git "):
                # command = input("git ").strip().split()
                if not command:
                    continue
                cmd = command[0]
                args = command[1:]
                
                if cmd == "add":
                    git_add(args)
                    continue
                elif cmd == "push":
                    git_push()
                    continue
                elif cmd == "clone":
                    if args:
                        git_clone(args[0])
                    else:
                        print("Error: Please provide a repository URL.")
                        continue
                elif cmd == "pull":
                    git_pull()
                    continue
                elif cmd == "init":
                    git_init()
                    continue
                elif cmd in ["exit", "quit"]:
                    print("Exiting Git Interface.")
                    break
                else:
                    print(f"Unknown command: {cmd}")

            if command.startswith("mkdir "):
                try:
                    path = command.split(" ", 1)[1].strip()  # Extract folder name
                    os.makedirs(path, exist_ok=True)       # Create the directory 
                except Exception as e:
                    print(f"mkdir: {e}")
                continue
            
            if command.startswith("rm "):
                path=command[len("rm "):].strip()

                if os.path.isfile(path):
                    os.remove(path)
                    print(f"Removed {GREEN}{path}{RESET} successfully")
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"Removed {GREEN}{path}{RESET} and its content successfully")
                else:
                    print(f"{RED}{path}{RESET} no such file or directory")
                continue

            if command == "clear":
                os.system("clear" if os.name != "nt" else "cls")
                continue

            if command == "ls":
                if len(command.split(" "))>1:
                    path=command.split(" ")[1:]
                else:
                    path="."
                if os.path.exists(path) and os.path.isdir(path):
                    files=os.listdir(path)
                    sys.stdout.write("\n".join(files) + "\n")
                else:
                    print(f"ls: cannot access {RED}{path}{RESET}: No such file or directory")            
                continue

            if command == "pwd":
                print("\033[34m\n" + os.getcwd() + "\033[0m\n")
                continue
            
            if command =="help":
                print("Available commands:")
                for cmd, desc in commands.items():
                    print(f"  {cmd:<15} - {desc}")
                print()
                continue

            if command.startswith("cd "):
                if command == "cd ~":
                    home_directory = os.path.expanduser("~")
                    os.chdir(home_directory)
                    continue
                try:
                    path = command.split(" ", 1)[1].strip()
                    os.chdir(path)  # Change the current working directory
                except FileNotFoundError:
                    print(f"cd: {RED}{path}{RESET}: No such file or directory")
                except IndexError:
                    print("{RED}cd: Missing argument{RESET}")
                continue



            if command.startswith("touch "):
                try:
        # Extract multiple file names
                    file_names = command.split(" ")[1:]
                    for file_name in file_names:
                        with open(file_name, "a"):
                            os.utime(file_name, None)
                except Exception as e:
                    print(f"touch: {e}")
                continue



            if command.startswith("type "):
                cmd = command[len("type "):].strip()
                if cmd in builtin_cmd:
                    print(f"{GREEN}{cmd} is a shell builtin{RESET}")
                    continue

                cmd_path = None
                paths = PATH.split(":")

                for path in paths:
                    potential_path = os.path.join(path, cmd)
                    if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                        cmd_path = potential_path
                        break

                if cmd_path:
                    print(f"{cmd} is {cmd_path}")

                else:
                    print(f"{cmd}: not found")
                continue
            
            elif shutil.which(command.split(" ")[0]): #checks external programs
                    os.system(command)  
            
            elif command == "exit":
                sys.exit(0)
            elif command.startswith("echo "):
                args = command[len("echo "):].strip()
                args_list = args.split('"')  # Split by double quotes
                cleaned_args = []

                for part in args_list:
                    if part:
                        cleaned_args.append(part.strip())

                args_list_single = " ".join(cleaned_args).split("'")  # Split by single quotes
                final_args = []

                for part in args_list_single:
                    if part:
                        final_args.append(part.strip())

                # Join the arguments with a single space
                result = " ".join(final_args)
                sys.stdout.write(result + "\n")
                continue

            elif command == "systeminfo":
                try:
                    result = subprocess.run("systeminfo", text=True, capture_output=True)
                    print(result.stdout)  # Print the system info output
                except FileNotFoundError:
                    print(f"{RED}systeminfo: command not found{RESET}")
                continue

            else:
                print(f"{RED}{command}: not found{RESET}")

 

if __name__ == "__main__":
    main()


