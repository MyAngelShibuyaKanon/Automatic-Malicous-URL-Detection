def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

from features import FeaturesFinder
import time
import pickle
import sklearn
loaded_model = pickle.load(open('model.pkl', "rb"))
start_time = time.time()
link = "https://www.kaggle.com/general/216555"
obj = FeaturesFinder(link)
Features = obj.getFeaturesList()
print(Features)



url = Features.pop(0)
print(url)
y_predicted = loaded_model.predict([Features])
print(y_predicted)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
