import tensorflow as tf
dataset1 = tf.data.Dataset.range(0, 3)
dataset2 = tf.data.Dataset.range(100, 103)
sample_dataset = tf.data.Dataset.sample_from_datasets(datasets=[dataset1, dataset2], rerandomize_each_iteration=None)