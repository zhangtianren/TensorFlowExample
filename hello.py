Import tensorflow as tf
#coding=utf-8


hello = tf.constant('hello, my tensorflow' ) 

sess = tf.Session()

print sess.run(hello)

a = tf.constant(10)

b = tf.constant(25)

print sess.run(a+b)

