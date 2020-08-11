import re
import urllib.request
response=urllib.request.urlopen("http://example.webscrapping.com/places/default/view/India-102")

html=response.read()
text=html.decode()
re.findall('<td class="w2p_fw">(.*?)</td>',text)
