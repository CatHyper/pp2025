import subprocess

while True:
    try:
        command = input("> ")
        if not command:
            continue
        if command.lower() == "exit":
            break
        process = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if process.stdout:
            print(process.stdout.strip())
        if process.stderr:
            print(process.stderr.strip())
    except Exception as e:
        print(f"An error occurred: {e}")
