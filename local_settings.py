'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC46f44e38a7c3abe7db848404e1513ef9" 
AUTH_TOKEN = "a2dfdd135507696c31353d0ac0fe685a"
BSSSPAM_APP_SID = "AP4d75d1c1760e246baf4f38e9049eede8"
BSS_SPAM_ID = "+19165028912"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
