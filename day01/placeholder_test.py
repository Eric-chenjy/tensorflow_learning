'''
@author :Eric-chen
@contact:809512722@qq.com
@time   :2018/4/15 10:33
@desc   :placeholder  占位的
'''
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 第一个占位符
input1 = tf.placeholder(tf.float32)
# 第二个占位符
input2 = tf.placeholder(tf.float32)

Output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(Output, feed_dict={input1: [10], input2: [20]}))
