import subprocess
import io
# subprocess.run('ls')
# subprocess.run('ls -la',shell=True)
# subprocess.run('dir')
# subprocess.run('dir',shell=True)
#case:-1
# output = subprocess.run(["ls","-la"])
# print(output)
# print(output.args)
# print(output.returncode)
# print(output.stdout)
#case:-2
# output = subprocess.run(["ls","-la"],capture_output=True)
# print(output.stdout.decode())
# print(output)
# print(output.args)
# print(output.returncode)
# output = subprocess.run(["ls","-la"],capture_output=True,text=True)

################################################################
###############pipe line the stdout only #######################
################################################################
output = subprocess.run(["ls","-la"],stdout=subprocess.PIPE)

