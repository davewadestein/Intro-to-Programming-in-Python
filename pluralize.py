import re

def pluralize(noun):
    """Use regular expressions to pluralize a word"""

    # ends in s or x or z
    if re.search('[sxz]$', noun): 
        return noun + 'es'
    # ends in h, but preceded by any letter other aeioudgkprt
    elif re.search('[^aeioudgkprt]h$', noun):
        return noun + 'es'
    # ends in y, preceded by a consonant
    elif re.search('[^aeiou]y$', noun):      
        return re.sub('y$', 'ies', noun)     
    else:
        return noun + 's'
