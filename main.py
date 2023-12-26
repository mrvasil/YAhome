from contextlib import redirect_stdout
from io import StringIO

from server import app

import webview


if __name__ == '__main__':
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('Smart Home', app, height=670, width=1080, background_color='#120b27')
        webview.start()


#import webview
#
#class Api:
#    def test1(self):
#        return 1+1
#
#    def test2(self):
#        return 2+2
#    
#api = Api()
#
#
#
#def create_interface():
#    html_content = open("interface/index.html", "r").read()
#    #test_var = "hmmmmmmmm?????"
#    #newline = '\n'
#    #with open('interface/index.html', 'r') as file:
#    #    html_content = f"{file.read().replace(newline, '')}".format(**locals())
#    
#    #webview.create_window("Test Interface", html=html_content, js_api=api, background_color="#1d1a2c")
#    webview.create_window("Test Interface", js_api=api, background_color="#000000", url="http://127.0.0.1:3000/")
#
#if __name__ == '__main__':
#    create_interface()
#    webview.start(http_server=True)