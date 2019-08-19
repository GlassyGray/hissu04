import tensorflow as tf

x_data = [[1,2,3],[4,5,6]]
X = tf.placeholder(tf.float32, [None,3])
W = tf.Variable(tf.random_normal([3,2]))
b = tf.Variable(tf.random_normal([2,1]))
expr = tf.matmul(X, W) + b

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print("=== x ===")
print(x_data)
print("=== X ===")
print(sess.run(X,feed_dict={X:[[1,2,3],[4,5,6],[7,8,9]]}))
print("=== W ===")
print(sess.run(W))
print("=== b ===")
print(sess.run(b))
print("=== expr ===")
print(sess.run(expr, feed_dict={X:x_data}))

sess.close()
