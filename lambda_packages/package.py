import shutil
import os
import zipfile
from distutils.dir_util import copy_tree

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

def copy_basics(dest):
    copy_tree('../models', './' + dest + '/models')
    copy_tree('../controllers', './' + dest + '/controllers')
    copy_tree('../shared_modules', './' + dest + '/shared_modules')

copy_basics('dni-number-assignment-lambda')
copy_basics('dni-refresh-ttl')
copy_basics('dni-reserve-numbers-lambda')
copy_basics('dni-answer-call-lambda')
copy_basics('dni-end-call-lambda')
copy_basics('dni-get-code-lambda')
copy_basics('dni-get-numbers-lambda')

copy_tree('../services/number_assignment', 'dni-number-assignment-lambda/services/number_assignment')
copy_tree('../services/reserve_number_pool', 'dni-reserve-numbers-lambda/services/')
copy_tree('../services/handle_inbound_call_from_twilio', 'dni-answer-call-lambda/services/')
copy_tree('../services/handle_inbound_call_end_from_twilio', 'dni-end-call-lambda/services/')
copy_tree('../services/generate_javascript_code', 'dni-get-code-lambda/services/')
copy_tree('../services/request_pool_numbers', 'dni-get-numbers-lambda/services/')

zipf = zipfile.ZipFile('dni-number-assignment-lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./dni-number-assignment-lambda', zipf)
zipf.close()

zipf = zipfile.ZipFile('dni-refresh-ttl.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./dni-refresh-ttl', zipf)
zipf.close()

zipf = zipfile.ZipFile('dni-reserve-numbers-lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./dni-reserve-numbers-lambda', zipf)
zipf.close()

zipf = zipfile.ZipFile('dni-answer-call-lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./dni-answer-call-lambda', zipf)
zipf.close()

zipf = zipfile.ZipFile('dni-end-call-lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./dni-end-call-lambda', zipf)
zipf.close()

zipf = zipfile.ZipFile('dni-get-code-lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./dni-get-code-lambda', zipf)
zipf.close()

zipf = zipfile.ZipFile('dni-get-numbers-lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./dni-get-numbers-lambda', zipf)
zipf.close()
