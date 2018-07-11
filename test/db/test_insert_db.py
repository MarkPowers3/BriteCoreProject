from orm.risk import Risk
from orm.base import Session, engine, Base
from orm.field import Field
from orm.option import Option

Base.metadata.create_all(engine)

session = Session()

session.query(Option).delete()
session.query(Field).delete()
session.query(Risk).delete()

#auto risk
auto = Risk("Automobile", "PAUTO")

auto_year = Field("Year", "year", "number", 4, auto)
auto_make = Field("Make", "make", "text", 10, auto)
auto_model = Field("Model", "model", "text", 10, auto)
auto_dtReg = Field("Date Registered", "date_registered", "date", None, auto)

auto_bodily = Field("Bodily Injury to Others", "bi", "enum", None, auto)
auto_pip = Field("Personal Injury Protection", "pip", "enum", None, auto)
auto_damage = Field("Damage to Someone Else's Property", "damage", "enum", None, auto)
auto_medical = Field("Medical", "medical", "enum", None, auto)
auto_deductible = Field("Collision Deductible", "deductible", "enum", None, auto)

#deductible
deductble1 = Option("100", "$100", auto_deductible)
deductble2 = Option("250", "$250", auto_deductible)
deductble3 = Option("500", "$500", auto_deductible)

#liability
liability1 = Option("100000", "$100,000", auto_damage)
liability2 = Option("250000", "$250,000", auto_damage)
liability3 = Option("500000", "$500,000", auto_damage)

bodily1 = Option("5000/10000", "$5,000/$10/000", auto_bodily)
bodily2 = Option("10000/20000", "$10,000/$20/000", auto_bodily)
bodily3 = Option("20000/40000", "$20,000/$40/000", auto_bodily)

pip1 = Option("5000", "$5,000", auto_pip)
pip2 = Option("8000", "$8,000", auto_pip)
pip3 = Option("10000", "$10,000", auto_pip)

medical1 = Option("5000", "$5,000", auto_medical)
medical2 = Option("5000", "$5,000", auto_medical)
medical3 = Option("5000", "$5,000", auto_medical)

# home risk
home = Risk("Home", "HOME")

home_address1 = Field("Address Line 1", "addressLine1", "text", 30, home)
home_address2 = Field("Address Line 2", "addressLine2", "text", 30, home)
home_city = Field("City", "city", "text", 15, home)
home_state = Field("State", "state", "enum", None, home)
home_zip = Field("Zip Code", "zip_code", "number", 5, home)
home_years = Field("Num Yrs Occupied", "yrsOccupied", "number", 2, home)
home_dtPurch = Field("Date Purchased", "date_purchased", "date", None, home)
home_price = Field("Purchase Price", "purchase_price", "currency", 8, home)
home_form = Field("HO Form", "form", "enum", None, home)
home_dwell = Field("Dwelling", "dwelling", "currency", 8, home)
home_other = Field("Other Structures", "other", "currency", 8, home)
home_property = Field("Personal Property", "property", "currency", 8, home)
home_loss = Field("Loss of Use", "loss", "currency", 8, home)

state5 = Option("CT", "Connecticut", home_state)
state1 = Option("MA", "Massachusetts", home_state)
state2 = Option("ME", "Maine", home_state)
state3 = Option("NH", "New Hampshire", home_state)
state4 = Option("RI", "Rhode Island", home_state)

form1 = Option("HO3", "HO-3", home_form)
form2 = Option("H0O4", "HO-4", home_form)
form3 = Option("HO6", "HO-6", home_form)


session.add(auto)
session.add(home)

session.add(auto_year)
session.add(auto_make)
session.add(auto_model)
session.add(auto_dtReg)
session.add(auto_deductible)
session.add(auto_bodily)
session.add(auto_pip)
session.add(auto_damage)
session.add(auto_medical)

session.add(home_address1)
session.add(home_address2)
session.add(home_city)
session.add(home_state)
session.add(home_zip)
session.add(home_years)
session.add(home_dtPurch)
session.add(home_price)
session.add(home_form)
session.add(home_dwell)
session.add(home_other)
session.add(home_loss)
session.add(home_property)

session.add(liability1)
session.add(liability2)
session.add(liability3)

session.add(deductble1)
session.add(deductble2)
session.add(deductble3)

session.add(bodily1)
session.add(bodily2)
session.add(bodily3)

session.add(pip1)
session.add(pip2)
session.add(pip3)

session.add(medical1)
session.add(medical2)
session.add(medical3)

session.add(state1)
session.add(state2)
session.add(state3)
session.add(state4)
session.add(state5)

session.add(form1)
session.add(form2)
session.add(form3)

session.commit()
session.close()