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
            case ["exit", "0"]:
                return 0
            case ["echo", *args]:
                print(*args)
            case ["type", arg]:
                cmd = cmd_params_list[1]
                cmd_path = None
                paths = PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"
                
                if cmd in builtin_cmds:
                    print(f"{cmd} is a shell builtin")
                elif cmd_path:
                    print(f"{cmd} is {cmd_path}")
                else:
                    print(f"{cmd} not found")
            case _:
                print(f"{cmd_params_list[0]}: command not found")
        
if __name__ == "__main__":
    main()