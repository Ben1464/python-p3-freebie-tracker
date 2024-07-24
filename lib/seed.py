# seed.py

from models import session, Company, Dev, Freebie

def seed_data():
    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()
    session.commit()

    google = Company(name="Google", founding_year=1998)
    amazon = Company(name="Amazon", founding_year=1994)
    facebook = Company(name="Facebook", founding_year=2004)

    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")
    dev3 = Dev(name="Charlie")

    session.add_all([google, amazon, facebook, dev1, dev2, dev3])
    session.commit()

    freebie1 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=google)
    freebie2 = Freebie(item_name="Mug", value=5, dev=dev2, company=amazon)
    freebie3 = Freebie(item_name="Sticker", value=1, dev=dev3, company=facebook)

    session.add_all([freebie1, freebie2, freebie3])
    session
