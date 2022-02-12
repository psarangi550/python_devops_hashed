import subprocess

# with open("openseus.log","w") as f:
#     output =subprocess.run(["ls", "-la"],capture_output=True)
#     f.write(output.stdout.decode())
#     # print(output.stdout)
#     print("process completed successfully")

with open("debian.log","w") as f:
    output =subprocess.run(["ls", "-la"],stdout=f,text=True)
    # print(output.stdout)
    print("process completed successfully")