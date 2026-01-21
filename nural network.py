import tensorflow as tf
tf.compat.v1.enable_eager_execution()
vector1=tf.constant([1.0,2.0,3.0])
vector2=tf.constant([4.0,5.0,6.0])
result_vector =tf.add(vector1,vector2)
print("vector1:",vector1.numpy())
print("vector2:",vector2.numpy())
print("Resultant vector:",result_vector.numpy())
