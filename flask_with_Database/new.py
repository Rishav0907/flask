from main import db,Tech

db.create_all()

Rishav = Tech('Rishav',18)
Arpita = Tech('Arpita',17)

db.session.add_all([Rishav,Arpita])

db.session.commit()

print(Rishav.id)
print(Arpita.id)

# DELETE

delete_tech=Tech.query.get(1)
db.session.delete(delete_tech)
db.session.commit()

print(Tech.query.all())