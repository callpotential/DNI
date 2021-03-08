python -m pylint controllers --fail-under=9 -f colorized
python -m pylint services --fail-under=9 -f colorized
python -m pylint models --fail-under=9 -f colorized
python -m pylint shared_modules --fail-under=9 -f colorized
python -m coverage run -m unittest discover
python -m coverage report -m --fail-under 90