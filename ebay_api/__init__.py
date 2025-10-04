# __init__.py
from .orders import get_orders

__all__ = ["get_orders"]

# 这样就方便你直接：

from ebay_api import get_orders

# 而不必写完整路径 from ebay_api.orders import get_orders。