"""
Created on Wed Mar 22 21:47:22 2017

@author: Rohan
"""
import re
def remove(data):
    if not data:
        return data
    if not isinstance(data, basestring):
        return data
    try:
    # UCS-4
        patt = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
    # UCS-2
        patt = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return patt.sub('', data)


#def remove(text):
#    emoji_pattern = re.compile(
#        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
#        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
#        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
#        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
#        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
#        "+", flags=re.UNICODE)
#    x=emoji_pattern.sub(r'', text) # no emoji
#    return  x