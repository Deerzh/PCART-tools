from sklearn import linear_model
clf = linear_model.ElasticNet(1.0, 0.5, True, normalize=False, precompute='auto', max_iter=1000, copy_X=True, random_state=None, selection='cyclic')