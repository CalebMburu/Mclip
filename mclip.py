#! python3
# mclip.py - A multi-clipboard program

# Associates each piece of text with its key phrase
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

# Looks in the TEXT dict for the key phrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for the keyphrase copied to clipboard: {keyphrase}')
else:
    print(f'There is no text for the keyphrase: {keyphrase}')

