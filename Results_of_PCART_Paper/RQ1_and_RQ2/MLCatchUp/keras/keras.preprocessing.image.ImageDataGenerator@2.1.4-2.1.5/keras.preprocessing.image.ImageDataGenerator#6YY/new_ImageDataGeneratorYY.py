from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(featurewise_center=False, samplewise_center=False, brightness_range=None, validation_split=0.0)