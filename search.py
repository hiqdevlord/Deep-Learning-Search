import random
import os
import time
import process_config

no_of_configs = 1000
configs_computed = {}
stride = [1,2,3]
features = [2**i for i in range(5,10)]
seed_config = [ [ random.randint(0,2), random.randint(0,4) ] for i in range(6) ] #the config be stride, feature, stride, feature ...
best_accuracy = 0
no_of_improv_solns = 0
start_time = time.time()

def get_new_config(config):
#Returns back a new config by flipping one of the variables in the input config 
	ret_val = config 
	rand_layer = random.randint(0,5)
	rand_param = random.randint(0,1)
	if rand_param == 1:
		ret_val[rand_layer][rand_param] = random.randint(0,4)
	else:
		ret_val[rand_layer][rand_param] = random.randint(0,2)
	return ret_val

def config_to_tuple(config):
#helper function to make configs hashable
	temp = [tuple(i) for i in config]
	return tuple(temp)

if __name__ == '__main__':
	print("starting search at "+str(start_time))
	best_accuracy = process_config.process_config(seed_config,"seed")
	configs_computed[config_to_tuple(seed_config)] = best_accuracy

	for i in range(no_of_configs):
		while True:
			new_config = get_new_config(seed_config)
			if config_to_tuple(new_config) not in configs_computed:
				break
		os.makedirs("iter_"+str(i))		
		new_accuracy = process_config.process_config(new_config,"iter_"+str(i)+"/iter_"+str(i))
		configs_computed[config_to_tuple(new_config)] = new_accuracy

		if new_accuracy >= best_accuracy:
			no_of_improv_solns += 1
			best_accuracy = new_accuracy
			seed_config = new_config
			print ("Found new solution at "+str(time.time() - start_time)+
				" Iteration: "+str(i)+" Improvement Number: "+ str(no_of_improv_solns) +
				" Config: " + process_config.printconfig(seed_config) + " Accuracy: " + str(best_accuracy) )