import sys

import numpy as np
import tensorflow as tf

# tf.compat.v1.enable_eager_execution()  # 此处使用的是tensorflow 1.13.1 版本
from tf_lib.gcn_lib.vertex import gen_grid1

tf.enable_eager_execution()  # 此处使用的是tensorflow 1.12.0 版本

x=tf.constant([2,3,4,5])
y=tf.constant([20,30,40,50])
z=tf.add(x,y)

grid = gen_grid1(2)

tf.print("grid:",grid,output_stream=sys.stderr)