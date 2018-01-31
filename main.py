from tkinter import *
from tkinter.messagebox import showinfo
import requests
import re
import json


regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def reply(url_content, method_radio, url_api):
    url = url_content.get()
    method = method_radio.get()
    api = url_api.get()
    print(url, method, api)
    if url =='' or api =='' or method == '':
        show_mesages('Errors', 'Hay dien day du thong tin')
    # showinfo(title="popup", message=url_content.get() + ", " + method_radio.get() + ", " + url_api)
    else:
        if not regex.match(api) or not regex.match(url):
            show_mesages("Loi", 'Khong dung dinh dang url')
        else:
            if method == "GET":
                result = requests.get(api, url)
                print(result)
            else:
                result = requests.post(api, json.dumps(url))
                print(result)


def show_mesages(status, msg):
    showinfo(title=status, message=msg)

app = Tk()
app.title('TEST SERVICE')
app.geometry('300x300')
#app.iconbitmap('py-blue-trans-out.ico')
Label(app, text='URL:').pack(side=TOP)
url_content = Entry(app, bd = 3)
url_content.pack(side=TOP)

Label(app, text='API:').pack(side=TOP)
url_api = Entry(app, bd = 3)
url_api.pack(side=TOP)

Label(app, text='Method:').pack()
method_radio = StringVar()
get_method = Radiobutton(app, text='GET', variable=method_radio, value="GET")
get_method.select()
get_method.pack()

post_method = Radiobutton(app, text='POST', variable=method_radio, value="POST")
post_method.pack()


button_get_url = Button(app, text='Send', command=(lambda : reply(url_content, method_radio, url_api)))
button_get_url.pack(side=TOP)
mainloop()