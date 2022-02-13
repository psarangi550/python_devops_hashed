import os

os.system("ls")#this will provide the stdout for the command execution
print(os.system("ls")) #this is provide the pid i.e the process id


###using the spawnl to fetch the process is for the linux execution ### 

# print(os.spawnl(os.P_NOWAIT, "/usr/sh", 'ls -la'))#process id without waiting for execution
# print(os.spawnl(os.P_WAIT,"/usr/sh", 'ls -la'))#process id once completed execution 
# print(os.system('ps -H'))#this will provide the process id of all listed

###using the os.popen function to execute the bash command###
# os.popen('ls -la')#:-file output as to run this command 
# print(os.popen('ls -la'))#wrapper object which we can be readable
# print(type(os.popen('ls -la')))#wrapper class which we can be read or write
# output=os.popen('dir').read()
# print(output)
# print(os.popen('ls -la').read())

###trying on the windows system ###
print(os.spawnl(os.P_NOWAIT, "C:\\Windows\\System32\\cmd.exe", "dir"))
