from flask import Flask
from flask import request
from windows_toasts import WindowsToaster, ToastText1
import pickle
from features import FeaturesFinder
import time
start_time = time.time()
loaded_model = pickle.load(open('model.pkl', "rb"))
print("Model loading finished --- %s seconds ---" % (time.time() - start_time))
toaster = WindowsToaster('Python')
app = Flask(__name__)
newToast = ToastText1()



@app.route('/')
def index():
    return 'Hello world, lol'

@app.route('/post', methods=["POST"])
def receiver():
    url = request.headers.get('url')
    obj = FeaturesFinder(url)
    Features = obj.getFeaturesList()
    print(Features)
    start_time = time.time()
    url = Features.pop(0)
    y_predicted = loaded_model.predict([Features])
    print("Prediction processing finished --- %s seconds ---" % (time.time() - start_time))
    print("URL is: ", y_predicted)
    if y_predicted == 1:
        newToast.SetBody("URL '"+url+"' is safe!")
        toaster.show_toast(newToast)
    elif y_predicted == 0:
        newToast.SetBody("URL '"+url+"' is suspicious!")
        toaster.show_toast(newToast)
    elif y_predicted == -1:
        newToast.SetBody("URL '"+url+"' is malicious!")
        toaster.show_toast(newToast)
    return(url)

if __name__ == '__main__':
    app.run(debug=True)



# def print_url(url):
#    cleanurl = url.replace("-raburaiburaburaibuyeahhhh-", "/")
 #   cleanurl = cleanurl.replace("-qwestionmarkowoowo-", "?")
  #  print(cleanurl)
   # print(url)
    # return(url) 