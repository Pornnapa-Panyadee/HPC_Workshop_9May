import tensorflow as tf
# Check for GPU availability
if tf.config.list_physical_devices('GPU’):
   # Configure TensorFlow to use the first available GPU
   physical_devices = tf.config.list_physical_devices('GPU’)
   tf.config.experimental.set_memory_growth(physical_devices[0], True)
   logical_devices = tf.config.list_logical_devices('GPU’)
   print("Using GPU: {}".format(logical_devices[0]))
else:
   print("No GPU available, defaulting to CPU.")

# Define some sample data
x = tf.constant([[1., 2.], [3., 4.]], dtype=tf.float32)
y = tf.constant([[5., 6.], [7., 8.]], dtype=tf.float32)

# Perform matrix multiplication on GPU (if available)
with tf.device("/GPU:0" if tf.config.list_physical_devices('GPU’)
  else "/CPU:0"): z = tf.matmul(x, y)

# Print the result
print(z.numpy())