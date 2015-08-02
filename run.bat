@echo off
%~d0
cd %~p0
set PYTHONPATH=%PYTHONPATH%;C:\workspace_python\autotest;C:\workspace_python\autotest\adbtest_services;C:\workspace_python\autotest\adbtest_testcase
echo %PYTHONPATH%
set RESULT_PATH=C:\workspace_python\autotest\work\result

python adbtest_testcase\AdbTest1.py
