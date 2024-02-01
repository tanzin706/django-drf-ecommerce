import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:  ###Name in Factory is CategoryFactory so here it will be category_factory###
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory(name="test_cat")
        # Assert
        assert x.__str__() == "test_cat"


class TestBrandModel:  ###Name in Factory is BrandFactory so here it will be brand_factory###
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        obj = brand_factory(name="test_brand")
        # Assert
        assert obj.__str__() == "test_brand"


class TestProductModel:  ###Name in Factory is ProductFactory so here it will be product_factory###
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        obj = product_factory(name="test_ProduCt")
        # Assert
        assert obj.__str__() == "test_ProduCt"
