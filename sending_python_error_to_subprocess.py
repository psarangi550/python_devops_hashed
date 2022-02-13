import subprocess
# output=subprocess.run(["rm","dne"],capture_output=True,text=True,check=True)
# print(output.stdout)
# print(output.stderr)

#handling the  error by usibg the subprocess.CalledProcessError excepotion handling##

try:
    output=subprocess.run(["rm","dne"],capture_output=True,text=True,check=True)
except subprocess.CalledProcessError as e:#handling the exception 
    print(e)
else:
    print(output.stdout)
    print(output.stderr)
