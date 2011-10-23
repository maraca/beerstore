from django.db import models

BEVERAGE_TYPES = (
    ('B', 'Beer'),
    ('W', 'Wine'),
    ('O', 'Other'),
)
    

class Product(models.Model):
    """Basic Product Definition."""

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,
                                   null=True)
    slug = models.SlugField(max_length=120,
                            db_index=True,
                            unique=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    disabled = models.BooleanField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Beverage(Product):
    """Built to abstract Beer and Wine similarities."""
    
    SIZE_UNIT_TYPES = (
        ('OZ', 'OZ'),
    )

    CONTAINER_TYPES = (
        ('B', 'BTL'),
        ('C', 'CAN'),
    )

    alcohol = models.DecimalField(max_digits=5,
                                  decimal_places=2)
    company = models.ForeignKey('Company')
    # country : TODO
    size_unit = models.CharField(max_length=3, 
                                 choices=SIZE_UNIT_TYPES) # OZ , mm, Pack
    size_value = models.CharField(max_length=10) # 22, 4, 6, 750
    container = models.CharField(max_length=2,
                                 choices=CONTAINER_TYPES) # BTL, CAN, Box etc. 
    abv = models.DecimalField(max_digits=4,
                              decimal_places=2)
    

class BeverageStyle(models.Model):
    """Beverage style.

    eg: Ale / IPA / Lager / Cabernet etc. 
    """
    name = models.CharField(max_length=150)
    beverage_type = models.CharField(max_length=2,
                                     choices=BEVERAGE_TYPES)

    def __unicode__(self):
        return self.name

class WineStyle(BeverageStyle):

    class Meta:
        proxy = True


class BeerStyle(BeverageStyle):

    class Meta:
        proxy = True


class Beer(Product):
    """Beer Definition."""
    ibu = models.IntegerField()
    """
    Bitterness shown in International Bittering Units, where:
        - Low bitterness 0 - 20
        - Moderate bitterness 21 - 30
        - Noticeable bitterness 31 and over
    """
    style = models.ForeignKey('BeerStyle')# Ale / IPA / Lager / Cabernet 


class Wine(Product):
    """Wine Definition."""
    # region = 
    # vintage =
    style = models.ForeignKey('WineStyle') # 


class Company(models.Model):
    """Company name for Beverage."""

    beverage_type = models.CharField(max_length=2,
                                     choices=BEVERAGE_TYPES)
    name = models.CharField(max_length=255)
