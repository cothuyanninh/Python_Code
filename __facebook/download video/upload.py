import requests
access = 'EAAEBYgHRvq8BAOSrZBTw0QMU0BWPqOykawiaaAQuTJ6nmIJQkjnhZBV9VH0WZAVt77Oeh3ghszHJdt1qCBZCCK1JyIc6IAZCN0NkZBRjtJd7u7xdGf1rpkhdlZAHFZCp5VisINZBJSP7eWudqPr6EfS9a3O8ZBazoWRDZCQaPQ1ZCJlgPcQujPzDXKZAzNVzIYOJXWkCswxAP6JhHIwZDZD'
url='https://graph-video.facebook.com/1032508590214379/videos?access_token='+str(access)
path="1.mp4"
files={'file':open(path,'rb')}
flag=requests.post(url, files=files).text
print (flag)