from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(None, 'train', None, shuffle=True, random_state=42, remove=(), download_if_missing=True, return_X_y=False)
