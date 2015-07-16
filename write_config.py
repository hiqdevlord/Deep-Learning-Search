def write_solver(filename): 
  solver_file =  ''' net: "'''+filename+'.prototxt'+'''"
test_iter: 100
test_interval: 500
base_lr: 0.001
momentum: 0.9
weight_decay: 0.004
lr_policy: "fixed"
display: 100
max_iter: 5000
snapshot: 5000
snapshot_prefix: "'''+filename+'''"
solver_mode: CPU''' #IMP
  with open(filename,'w') as f:
    f.write(solver_file)

def write_net(config,filename):	
	stride = [1,2,3]
	features = [2**i for i in range(5,10)]
	config_file = '''
name: "CIFAR10_quick"
layer {
  name: "cifar"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform_param {
    mean_file: "./mean.binaryproto"
  }
  data_param {
    source: "./cifar10_train_lmdb"
    batch_size: 100
    backend: LMDB
  }
}
layer {
  name: "cifar"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TEST
  }
  transform_param {
    mean_file: "./mean.binaryproto"
  }
  data_param {
    source: "./cifar10_test_lmdb"        
    batch_size: 100
    backend: LMDB
  }
}

layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"  
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: '''+str(features[config[0][1]]) +'''
    pad: 1
    kernel_size: 3
    stride: '''+str(stride[config[0][0]])+'''
    weight_filler {
      type: "gaussian"
      std: 0.0001
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "conv1"
  top: "conv1"
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "conv1"  
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: '''+str(features[config[1][1]])+'''
    pad: 1
    kernel_size: 3
    stride: '''+str(stride[config[1][0]])+'''
    weight_filler {
      type: "gaussian"
      std: 0.0001
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu2"
  type: "ReLU"
  bottom: "conv2"
  top: "conv2"
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv2"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv3"
  type: "Convolution"
  bottom: "pool1"  
  top: "conv3"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: '''+str(features[config[2][1]])+'''
    pad: 1
    kernel_size: 3
    stride: '''+str(stride[config[2][0]])+'''
    weight_filler {
      type: "gaussian"
      std: 0.0001
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu3"
  type: "ReLU"
  bottom: "conv3"
  top: "conv3"
}
layer {
  name: "conv4"
  type: "Convolution"
  bottom: "conv3" 
  top: "conv4"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: '''+str(features[config[3][1]])+'''
    pad: 1
    kernel_size: 3
    stride: '''+str(stride[config[3][0]])+'''
    weight_filler {
      type: "gaussian"
      std: 0.0001
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu4"
  type: "ReLU"
  bottom: "conv4"
  top: "conv4"
}

layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv4"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}

layer {
  name: "conv5"
  type: "Convolution"
  bottom: "pool2"  
  top: "conv5"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: '''+str(features[config[4][1]])+'''
    pad: 1
    kernel_size: 3
    stride: '''+str(stride[config[4][0]])+'''
    weight_filler {
      type: "gaussian"
      std: 0.0001
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu5"
  type: "ReLU"
  bottom: "conv5"
  top: "conv5"
}
layer {
  name: "conv6"
  type: "Convolution"
  bottom: "conv5"  
  top: "conv6"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: '''+str(features[config[5][1]])+'''
    pad: 1
    kernel_size: 3
    stride: '''+str(stride[config[5][0]])+'''
    weight_filler {
      type: "gaussian"
      std: 0.0001
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu6"
  type: "ReLU"
  bottom: "conv6"
  top: "conv6"
}
layer {
  name: "pool3"
  type: "Pooling"
  bottom: "conv6"
  top: "pool3"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool3"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 64
    weight_filler {
      type: "gaussian"
      std: 0.1
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 10
    weight_filler {
      type: "gaussian"
      std: 0.1
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "accuracy"
  type: "Accuracy"
  bottom: "ip2"
  bottom: "label"
  top: "accuracy"
  include {
    phase: TEST
  }
}
layer {
  name: "loss"
  type: "SoftmaxWithLoss"
  bottom: "ip2"
  bottom: "label"
  top: "loss"
}
	'''
	with open(filename,"w") as f:
		f.write(config_file)

def write_config(config,filename):
  print("Writing Net to file: "+filename+'.prototxt')
  write_net(config,filename+'.prototxt')
  print('done')
  print("Writing solver to file: "+filename+'_solver.prototxt')
  write_solver(filename+'_solver.prototxt')
  print('done')
  print('All files written!')
  
  