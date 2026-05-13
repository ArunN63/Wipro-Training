@echo off

echo ================================
echo Running Robot Framework Tests
echo ================================

robot ^
-d reports ^
--output output.xml ^
--log automationlog.html ^
--report report.html ^
tests/

echo ================================
echo Test Execution Completed
echo ================================

pause