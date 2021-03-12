import os
import zipfile
from shutil import copytree, ignore_patterns, copyfile


def remove_first_folder_from_path(path: str):
    first_slash_idx = path.find('\\')
    return path[first_slash_idx + 1:]


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            destination_path = os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
            ziph.write(os.path.join(root, file),
                       remove_first_folder_from_path(destination_path))


def copy_basics(dest):
    copytree('../models', './' + dest + '/models')
    copytree('../controllers', './' + dest + '/controllers')
    copytree('../shared_modules', './' + dest + '/shared_modules')

copy_basics('dni-number-assignment-lambda')
copy_basics('dni-refresh-ttl')
copy_basics('dni-reserve-numbers-lambda')
copy_basics('dni-answer-call-lambda')
copy_basics('dni-end-call-lambda')
copy_basics('dni-get-code-lambda')
copy_basics('dni-get-numbers-lambda')

copytree('../services/number_assignment', 'dni-number-assignment-lambda/services/number_assignment', ignore=ignore_patterns('lambda_function.py'))
copytree('../services/reserve_number_pool', 'dni-reserve-numbers-lambda/services/reserve_number_pool', ignore=ignore_patterns('lambda_function.py'))
copytree('../services/handle_inbound_call_from_twilio', 'dni-answer-call-lambda/services/handle_inbound_call_from_twilio', ignore=ignore_patterns('lambda_function.py'))
copytree('../services/handle_inbound_call_end_from_twilio', 'dni-end-call-lambda/services/handle_inbound_call_end_from_twilio', ignore=ignore_patterns('lambda_function.py'))
copytree('../services/generate_javascript_code', 'dni-get-code-lambda/services/generate_javascript_code', ignore=ignore_patterns('lambda_function.py'))
copytree('../services/request_pool_numbers', 'dni-get-numbers-lambda/services/request_pool_numbers', ignore=ignore_patterns('lambda_function.py'))

copyfile('../services/number_assignment/lambda_function.py', 'dni-number-assignment-lambda/lambda_function.py')
copyfile('../services/reserve_number_pool/lambda_function.py', 'dni-reserve-numbers-lambda/lambda_function.py')
copyfile('../services/handle_inbound_call_from_twilio/lambda_function.py', 'dni-answer-call-lambda/lambda_function.py')
copyfile('../services/handle_inbound_call_end_from_twilio/lambda_function.py', 'dni-end-call-lambda/lambda_function.py')
copyfile('../services/generate_javascript_code/lambda_function.py', 'dni-get-code-lambda/lambda_function.py')
copyfile('../services/request_pool_numbers/lambda_function.py', 'dni-get-numbers-lambda/lambda_function.py')

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
