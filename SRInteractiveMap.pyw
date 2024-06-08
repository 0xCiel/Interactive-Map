import webview

window = webview.create_window('SR Interactive Map', 'https://star-rail-map.appsample.com/', on_top=True)
webview.start(window)