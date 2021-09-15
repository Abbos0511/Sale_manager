from app.views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'category',CategoryView,basename='category')
router.register(r'brand',BrandView,basename='brand')
router.register(r'product',ProductView,basename='product')
router.register(r'product-by-category',ProductByCategoryView,basename='product-by-category')
router.register(r'stock',StockView,basename='stock')
router.register(r'unit',UnitView,basename='unit')
router.register(r'price-history',PriceHistoryView,basename='price-history')
router.register(r'price-history-by-product',PriceHistoryByProductView,basename='price-history-by-product')
router.register(r'supplier',SupplierView,basename='supplier')
router.register(r'debit',DebitView,basename='debit')
router.register(r'seller',SellerView,basename='seller')
router.register(r'sale',SaleView,basename='sale')
router.register(r'sale-product',SaleProductView,basename='sale-product')
