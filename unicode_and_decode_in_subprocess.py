import subprocess

### now here we are handling as ### byte string using the universal newlines   ####

# output=subprocess.run(["python3", "test.py"],capture_output=True,input="abc\ndef",universal_newlines=True)

#here we are not using the decode option so keep in mind

# print(output.stdout)

# print(output.stderr)

#handle the same using the text option ####


output=subprocess.run(["python3", "test.py"],capture_output=True,input="abc\ndef",text=True)

#here we are not using the decode option so keep in mind

print(output.stdout)

print(output.stderr)



