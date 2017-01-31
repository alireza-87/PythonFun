# Just A Fun Python2.7 Script
# AlirezaKarimi
# Email:Alireza.karimi.67@gmail.com
# Tell:+989362397176

import re
inputString = ['www.gapafzar.com',
'www.gapafzar.com/join/asdljsdhnfljsdnfkljsd',
'www.gapafzar.com/asljdkaslkd',
'http://www.gapafzar.com/alsdhjkhasdjk',
'https://www.gapafzar.com/alsdhjasd',
'http://www.gapafzar.com/join/alsdhjkhasdjk',
'https://www.gapafzar.com/join/alsdhjasd',
'www.gapafzar.im',
'www.gapafzar.im/join/asdljsdhnfljsdnfkljsd',
'www.gapafzar.im/asljdkaslkd',
'http://www.gapafzar.im/alsdhjkhasdjk',
'https://www.gapafzar.im/alsdhjasd',
'http://www.gapafzar.im/join/alsdhjkhasdjk',
'https://www.gapafzar.im/join/alsdhjasd',
'www.gapafzar.ir',
'www.gapafzar.ir/join/asdljsdhnfljsdnfkljsd',
'www.gapafzar.ir/asljdkaslkd',
'http://www.gapafzar.ir/alsdhjkhasdjk',
'https://www.gapafzar.ir/alsdhjasd',
'http://www.gapafzar.ir/join/alsdhjkhasdjk',
'https://www.gapafzar.ir/join/alsdhjasd',
'www.gapafzar.id',
'www.gapafzar.id/join/asdljsdhnfljsdnfkljsd',
'www.gapafzar.id/asljdkaslkd',
'http://www.gapafzar.id/alsdhjkhasdjk',
'https://www.gapafzar.id/alsdhjasd',
'http://www.gapafzar.id/join/alsdhjkhasdjk',
'https://www.gapafzar.id/join/alsdhjasd']
pattern = '((http[s]?:\/\/(www\.)?|w{3}\.)*)(gapafzar\.+(com|im|ir|id)\/join(\/.*)|gapafzar\.+(com|im|ir|id)\/(\w{1,}))'
prog = re.compile(pattern)
for value in inputString:
    if prog.match(value):
        print " result : ", ' MATCH ', ' value : ', value
    else:
        print " result : ", ' FAIL  ', ' value : ', value
raw_input()
