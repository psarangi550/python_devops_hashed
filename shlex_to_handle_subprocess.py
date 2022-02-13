import subprocess
import shlex

##this is a potential threat as the user can provide any input##
# user_input=input("Enter the file you want to read")
# output=subprocess.run(f'cat {user_input}',shell=True,capture_output=True)
# print(output.stdout.decode())

###using shlex to handle it #####
# user_input=input("Enter the file you want to read")
# output=subprocess.run(f'cat {shlex.quote(user_input)}',shell=True,capture_output=True)
# print(output.stdout.decode())
# print(output.stderr.decode())

##even more securing using the  shlex.split()####
user_input=input("Enter the file you want to read")
output=subprocess.run(shlex.split(f'cat {shlex.quote(user_input)}'),capture_output=True)
print(output.stdout.decode())
print(output.stderr.decode())