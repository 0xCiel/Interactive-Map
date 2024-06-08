import webview

window = webview.create_window('GI Interactive Map', 'https://genshin-impact-map.appsample.com/', on_top=True)
webview.start(window)