import seaborn as sns
import pandas as pd
import webbrowser


url='https://en.wikipedia.org/wiki/Ambuja_Cements'
table_num = 0
df = pd.read_html(url)

# print(type(df[0]))
show = df[table_num].to_html()
print(type(show))

f = open('wikiTable.html', 'w', encoding="utf-8")

html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<div>"""
  
html_template2="""</div>
</body>
</html>
"""
s = str(html_template1+show+html_template2)
print(type(s))

f.write(s)

f.close()

webbrowser.open('wikiTable.html')