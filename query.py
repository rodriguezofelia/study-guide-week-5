"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# This is a query object that will return '<class 'flask_sqlalchemy.BaseQuery'>'.
# In order to return something, you would have to attach .all(), .one(), etc at
# the end of the query. 


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table manages a many to many relationship. 
# An association table acts like the middleperson among tables. It 
# will hold two foreign key - one from each table's primary key. 




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.get("ram")

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name = "Corvette", brand_id = "che").all()
q2_alt = Model.query.filter(Model.name=="Corvette", Model.brand_id == "che").all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
# starts with 'Cor%'
# contains word within '%Cor%'
# ends with '%Cor'
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued == None)).all() 
q6_alt = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id.like != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = Model.query.filter(Model.year==year).all()

    print(f"{year}")

    if models: 
        for model in models: 
            result = f"{model.name} {model.brand.name} {model.brand.headquarters}"
            print(result)

        print(f"{year}")
    else: 
        print("No models found for this year")

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    # brands = db.session.query(Brand.name, Brand.models).all()
    brands = Brand.query.all()

    for brand in brands: 
        print(f'-----{brand.name}-----')
        for model in brand.models:
            print(model.name, model.year)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return Brand.query.filter(Brand.name.like(f"%{mystr}%")).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()

