@echo off
echo ========================================
echo OrangeHRM BDD Test Suite
echo ========================================
echo.

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt > nul

REM Run tests with different tags
echo.
echo Select test type:
echo 1. Run all tests
echo 2. Run Smoke tests only
echo 3. Run Regression tests only
echo 4. Run specific feature
echo.

set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    echo Running all tests...
    pytest -v -s
) else if "%choice%"=="2" (
    echo Running Smoke tests...
    pytest -v -s -m smoke
) else if "%choice%"=="3" (
    echo Running Regression tests...
    pytest -v -s -m regression
) else if "%choice%"=="4" (
    echo Available features:
    echo 1. login
    echo 2. employee_management
    echo 3. admin_search
    echo 4. leave_workflow
    echo 5. profile_update
    set /p feature="Enter feature name: "
    pytest -v -s features/%feature%.feature
) else (
    echo Invalid choice!
)

echo.
echo Tests completed! Check report.html for results.
pause