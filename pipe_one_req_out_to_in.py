import subprocess

# output =subprocess.run(['cat','text.txt'],capture_output=True,check=True,text=True)

# # print(output.args)
# # print(output.returncode)
# # print(output.stdout)

# ################################################################
# #now inputing the output result as the inpput for the grep command
# ################################################################

# return_output =subprocess.run(['grep', '-n','-i','text'],capture_output=True,check=True,text=True,input=output.stdout)

# print(return_output.args)
# print(return_output.returncode)
# print(return_output.stdout)


################################################################
##Alternate approch using the direct piping by the shell=True command
################################################################

output = subprocess.run("cat text.txt | grep -i -n 'text' ",shell=True,capture_output=True,text=True)

print(output.stdout)
print(output.returncode)