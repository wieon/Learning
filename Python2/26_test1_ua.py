import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode('utf-8')
print(html)

