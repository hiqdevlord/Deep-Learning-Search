#!/usr/bin/env python
"""
Draw a graph of the net architecture.
"""
from google.protobuf import text_format

import caffe
import caffe.draw
from caffe.proto import caffe_pb2

def draw_net(net_file,op_file,rankdir='LR'):
    #args = parse_args()
    net = caffe_pb2.NetParameter()
    text_format.Merge(open(net_file).read(), net)
    print('Drawing net to %s' % op_file)
    caffe.draw.draw_net_to_file(net, op_file, rankdir)
