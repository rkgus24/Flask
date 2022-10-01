import scipy.io
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

train_data = scipy.io.loadmat('extra_32x32.mat')

X = train_data['X']
y = train_data['y']

X = X.reshape(X.shape[0] * X.shape[1] * X.shape[2], X.shape[3]).T
y = y.reshape(y.shape[0], )

X, y = shuffle(X, y, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

joblib.dump(clf, '../model/model/pkl')
