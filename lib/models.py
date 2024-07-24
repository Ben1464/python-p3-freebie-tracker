# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, declarative_base

Base = declarative_base()
engine = create_engine('postgresql://user:password@localhost/freebie_db')
Session = sessionmaker(bind=engine)
session = Session()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)

    freebies = relationship('Freebie', backref='company', lazy=True)

    @property
    def devs(self):
        return list(set([freebie.dev for freebie in self.freebies]))

    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    freebies = relationship('Freebie', backref='dev', lazy=True)

    @property
    def companies(self):
        return list(set([freebie.company for freebie in self.freebies]))

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

Base.metadata.create_all(engine)
