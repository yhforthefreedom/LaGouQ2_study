import os

# 项目路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试数据路径
test_case_path = os.path.join(project_path, "test_data", "test_data.xlsx")
# 测试报告路径
test_report_path = os.path.join(project_path, "test_result", "html_report", "test_api.html")
# 配置文件路径
test_config_path = os.path.join(project_path, "conf", "case.config")
# 日志文件路径
test_log_path = os.path.join(project_path, "test_result", "log", "my_log.txt")
