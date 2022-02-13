import subprocess

with open("text1.txt", "r") as f:
    output=subprocess.run(['python3', 'test.py'],capture_output=True,text=True,stdin=f)
    print(output.stdout)
    print(output.stderr)
    
