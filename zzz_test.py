from tests.constants_for_test import get_test_environment_urls
from trade_xm_app.models import OrderStatusEnum

status = OrderStatusEnum.PENDING

# print(status)


url_1, _url2 = get_test_environment_urls()
print(url_1)
print(_url2)

