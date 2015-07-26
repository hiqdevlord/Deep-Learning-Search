import random
import os
import time
import process_config
import cPickle as pickle
import traceback

no_of_configs = 1000
i = 0
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

def load_from_prev():
	if os.path.isfile('iters_so_far.save'):
		i = pickle.load(open('iters_so_far.save','rb'))
		print 'iterations so far loaded'
	
	if os.path.isfile("configs_computed.save"):
		configs_computed = pickle.load(open("configs_computed.save","rb"))
		print('computed configs loaded')
	
	if os.path.isfile("best_config.save"):
		seed_config = pickle.load(open("best_config.save",'rb'))
		print('best config loaded')
	
	if os.path.isfile("best_accuracy.save"):
		best_accuracy = pickle.load(open("best_accuracy.save",'rb'))
		print('best accuracy loaded')
	
	if os.path.isfile('no_of_improv_solns.save'):
		no_of_improv_solns = pickle.load(open('no_of_improv_solns.save','rb'))
		print('no of improved solutions loaded')

if __name__ == '__main__':
	load_from_prev()
	try:
		print("starting search at "+str(start_time))
		best_accuracy = process_config.process_config(seed_config,"seed")
		configs_computed[config_to_tuple(seed_config)] = best_accuracy
		print i
		print no_of_configs

		while i < no_of_configs:
			while True:
				new_config = get_new_config(seed_config)
				if config_to_tuple(new_config) not in configs_computed:
					break
			i+=1
			#os.makedirs("iter_"+str(i))		
			new_accuracy = process_config.process_config(new_config,"iter_"+str(i))
			configs_computed[config_to_tuple(new_config)] = new_accuracy

			if new_accuracy > best_accuracy:
				no_of_improv_solns += 1
				best_accuracy = new_accuracy
				seed_config = new_config
				print ("Found new solution at "+str(time.time() - start_time)+
					" Iteration: "+str(i)+" Improvement Number: "+ str(no_of_improv_solns) +
					" Config: " + process_config.printconfig(seed_config) + " Accuracy: " + best_accuracy )
	
	except :
		print("exception caught,dumping computed results to files")
		print('******************************	Stack Trace    ******************************')
		traceback.print_exc()
		pickle.dump(i,open('iters_so_far.save','wb'))
		pickle.dump(configs_computed,open("configs_computed.save","wb"))
		pickle.dump(seed_config,open("best_config.save",'wb'))
		pickle.dump(best_accuracy,open("best_accuracy.save",'wb'))
		pickle.dump(no_of_improv_solns,open('no_of_improv_solns.save','wb'))
	print("starting search at "+str(start_time))
	best_accuracy = process_config.process_config(seed_config,"seed")
	configs_computed[config_to_tuple(seed_config)] = best_accuracy

	for i in range(no_of_configs):
		while True:
			new_config = get_new_config(seed_config)
			if config_to_tuple(new_config) not in configs_computed:
				break
		os.makedirs("iter_"+str(i),exist_ok=True)		
		new_accuracy = process_config.process_config(new_config,"iter_"+str(i)+"/iter_"+str(i))
		configs_computed[config_to_tuple(new_config)] = new_accuracy

		if new_accuracy >= best_accuracy:
			no_of_improv_solns += 1
			best_accuracy = new_accuracy
			seed_config = new_config
			print ("Found new solution at "+str(time.time() - start_time)+
				" Iteration: "+str(i)+" Improvement Number: "+ str(no_of_improv_solns) +
				" Config: " + process_config.printconfig(seed_config) + " Accuracy: " + str(best_accuracy) )
