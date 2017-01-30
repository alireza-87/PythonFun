# Just A Fun Python2.7 Script
# AlirezaKarimi
# Email:Alireza.karimi.67@gmail.com
# Tell:+989362397176

import re
inputString = ['https://www.gapafzar.com/groupname','http://www.gapafzar.com/groupname','www.gapafzar.com/groupname','https://www.gapafzar.com/groupname/Test','http://www.gapafzar.com/groupname/Test','www.gapafzar.com/groupname/Test','www.google.com','asdhttps://www.gapafzar.com/groupname/Test']
pattern = '(http[s]?:\/\/(www\.)?|w{3}\.)(gapafzar\.com\/join(\/.*)|gapafzar\.com\/(\w{1,}))'
prog = re.compile(pattern)
for value in inputString:
    if prog.match(value):
        print " result : ", ' MATCH ', ' value : ', value
    else:
        print " result : ", ' FAIL  ', ' value : ', value
raw_input()
