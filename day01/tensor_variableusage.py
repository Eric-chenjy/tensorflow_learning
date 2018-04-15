'''
@author :Eric-chen
@contact:809512722@qq.com
@time   :2018/4/15 10:04
@desc   :tensorflow变量的定义和使用方法
'''
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 定义一个变量初始值是0，名字叫count（目前觉得state就是一个op，在TensorFlow中，所有的操作op，变量都视为节点）
state = tf.Variable(1, name='counter')
# 打印state的名字  counter:0
print(state.name)
# 用tensorflow做一个操作给这个变量循环加一个数5 并且打印
one = tf.constant(1)
result = tf.add(state, one)
update = tf.assign(state, result)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
