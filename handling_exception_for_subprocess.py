import subprocess

#case:-1
# output=subprocess.run(['ls', '-la','dne'],stdout=subprocess.PIPE)
# print(output.returncode)
# print(output.stderr)
#case:-2
# output=subprocess.run(['ls', '-la','dne'],stderr=subprocess.PIPE)
# print(output.returncode)
# print(output.stderr)
#case:-3:-i want python to throw an error while accessing the stderr
# output=subprocess.run(['ls', '-la','dne'],check=True,capture_output=True)
# print(output.returncode)
# print(output.stderr)
#case:-4:-handle the stderr error to redirect to the suprocess.DEVNULL direcory
output=subprocess.run(['ls', '-la','dne'],stderr=subprocess.DEVNULL,text=True)
print(output.returncode)
print(output.stderr)
