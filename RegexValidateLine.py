# Just A Fun Python2.7 Script
# AlirezaKarimi
# Email:Alireza.karimi.67@gmail.com
# Tell:+989362397176

import re
#pattern = '(http[s]?:\/\/(www\.)?|w{3}\.)(gapafzar\.com\/join(\/.*)|gapafzar\.com\/(\w{1,}))'
pattern=raw_input("Enter Your RegEx : ")
inputString=raw_input("Enter Your String : ")
prog = re.compile(pattern)
if prog.match(inputString):
    print " result : ", ' MATCH '
else:
    print " result : ", ' FAIL  '
raw_input()
