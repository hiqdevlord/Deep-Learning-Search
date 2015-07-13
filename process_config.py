from write_config import write_config
from draw_net import draw_net
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

def get_accuracy_from_log(filename): #TODO
	pass
def process_config(config,filename):

	print("Processing config: "+printconfig(config))
	print("Writing config to file:"+filename+'.prototxt')
	write_config(config,filename+'.prototxt')
	print("done")
	print("Visualizing Config")
	draw_net(filename+'.prototxt',filename+".png")
	print("running config,using solver in solver.prototxt")
	print("saving log to"+filename+".log")
	#TODO code to run the config 
	accuracy = get_accuracy_from_log(filename+'.log') 
	print ("gave accuracy: " + str(accuracy))
	return accuracy
		