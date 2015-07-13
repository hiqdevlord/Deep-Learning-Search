import subprocess

output = subprocess.check_output(['tail','-n4','test'])
output = output.split('\n')[0]
print float(output.split('accuracy = ')[1])
