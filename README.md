# python
Чтобы сформировать отчет Allure, сначала выполните команду для запуска тестов:
pytest --alluredir reports/allure_raw

Затем сформируйте отчет:
allure generate reports/allure_raw -o reports/allure_report


И, наконец, откройте отчет в браузере:
allure open reports/allure_report
