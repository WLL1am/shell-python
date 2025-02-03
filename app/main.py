import sys
import os

def main():
    
    builtin_cmds = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH")
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Retrive and parse user input
        cmd_params = input()
        cmd_params_list = cmd_params.split(" ")
        
        match cmd_params_list:
            case ["type", arg] if arg in builtin_cmds:
                print(f"{arg} is a shell builtin")
            case ["type", arg] if arg not in builtin_cmds:
                print(f"{arg}: not found")
            case ["exit", "0"]:
                return 0
            case ["echo", *args]:
                print(*args)
            case _:
                print(f"{cmd_params_list[0]}: command not found")
        
    
    
if __name__ == "__main__":
    main()