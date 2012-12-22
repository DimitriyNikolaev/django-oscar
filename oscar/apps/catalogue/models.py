"""
Vanilla product models
"""
from oscar.apps.catalogue.abstract_models import *
from django.db import models

class ProductClass(AbstractProductClass):
    pass


class Category(AbstractCategory):
    displayname = models.CharField('DisplayName', max_length=255, db_index=True)

class ProductCategory(AbstractProductCategory):
    pass


class Product(AbstractProduct):
    pass


class ContributorRole(AbstractContributorRole):
    pass


class Contributor(AbstractContributor):
    pass


class ProductContributor(AbstractProductContributor):
    pass


class ProductAttribute(AbstractProductAttribute):
    pass


class ProductAttributeValue(AbstractProductAttributeValue):
    pass


class AttributeOptionGroup(AbstractAttributeOptionGroup):
    pass


class AttributeOption(AbstractAttributeOption):
    pass


class AttributeEntity(AbstractAttributeEntity):
    pass


class AttributeEntityType(AbstractAttributeEntityType):
    pass


class Option(AbstractOption):
    pass


class ProductImage(AbstractProductImage):
    pass
