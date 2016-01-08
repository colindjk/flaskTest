from app import db
from models import BlogPost

# create the db and the db 
db.create_all()

#insert etc
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

# commit the changes
db.session.commit()
