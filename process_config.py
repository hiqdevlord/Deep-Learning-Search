from write_config import write_config
#from draw_net import draw_net
import subprocess

def printconfig(config): 
	stride = [1,2,3]
	features = [2**i for i in range(5,10)]
	ret_val = (
		(stride[config[0][0]], features[config[0][1]]),
		(stride[config[1][0]], features[config[1][1]]),
		(stride[config[2][0]], features[config[2][1]]),
		(stride[config[3][0]], features[config[3][1]]),
		(stride[config[4][0]], features[config[4][1]]),
		(stride[config[5][0]], features[config[5][1]]) 
		)
	return str(ret_val)

def get_accuracy_from_log(filename):
	output = subprocess.check_output(['tail','-n4',filename])
	output = output.split('\n')[0]
	return float(output.split('accuracy = ')[1])

def process_config(config,filename):
	print("Processing config: "+printconfig(config))
	print("Writing required files")
	write_config(config,filename)
	print("done")
	#print("Visualizing Config")
	#draw_net(filename+'.prototxt',filename+".png")
	print("running config,using solver in "+filename+"_solver.prototxt")
	print("saving log to "+filename+".log")
	#subprocess.call(['touch',filename+'.log'])
	text = '''./tools/caffe train -solver='''+filename+"_solver.prototxt>"+filename+'.log'+" 2>&1"
	print text
	subprocess.call([text],shell=True) 
	accuracy = get_accuracy_from_log(filename+'.log') 
	print ("gave accuracy: " + str(accuracy))
	return accuracy
	
		
