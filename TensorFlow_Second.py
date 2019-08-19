import tensorflow as tf
import numpy as np

x_data=[1,2,3]
y_data=[4,5,6]

W=tf.Variable(tf.random_normal([1]))
b=tf.Variable(tf.random_normal([1]))

X=tf.placeholder(tf.float32, name="X")
Y=tf.placeholder(tf.float32, name="Y")
print(X)
print(Y)

hypothesis = W*X+b

cost = tf.reduce_mean(tf.square(hypothesis-Y))

optimaizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train_op = optimaizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(601):
    _, cost_val = sess.run([train_op, cost], feed_dict={X: x_data, Y: y_data})
    print(step, cost_val, sess.run(W), sess.run(b))

print("\n=== Test ===")
print("X: 5, Y:", sess.run(hypothesis, feed_dict={X: 5}))
print("X: 2.5, Y:", sess.run(hypothesis, feed_dict={X: 2.5}))

sess.close()