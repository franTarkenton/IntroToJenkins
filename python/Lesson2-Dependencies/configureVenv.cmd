:: Bundle up the commands to create a Virtualenv
:: for python3 env
SET VENVPATH=<path for where your venv should get created goes here>
SET CWD=%cd%

python -m venv %VENVPATH%
%VENVPATH%\Scripts\activate
