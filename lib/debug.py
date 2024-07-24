# debug.py

from models import session, Company, Dev, Freebie

# Create sample data
google = session.query(Company).filter_by(name="Google").first()
alice = session.query(Dev).filter_by(name="Alice").first()
bob = session.query(Dev).filter_by(name="Bob").first()

# Test relationships
print(google.freebies)          # Should return a list of freebies from Google
print(alice.companies)          # Should return a list of companies Alice received freebies from

# Test methods
google.give_freebie(alice, "Hat", 15)
print(google.freebies)          # Should include the new freebie "Hat"
print(alice.received_one("Hat"))  # Should return True

freebie = session.query(Freebie).filter_by(item_name="Hat").first()
print(freebie.print_details())  # Should print "Alice owns a Hat from Google"

alice.give_away(bob, freebie)
print(freebie.print_details())  # Should print "Bob owns a Hat from Google"
