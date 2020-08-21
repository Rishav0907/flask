from main import db , Tech


#CREATE

my_Tech=Tech('Pretam',5)
db.session.add(my_Tech)
db.session.commit()

# READ

all_Tech=Tech.query.all() #List of Tech objects

print(all_Tech)

# SELECT BY ID
Tech_first=Tech.query.get(1)
print(Tech_first.name)

# FILTERS

Tech_filter=Tech.query.filter_by(name='Rishav')
print(Tech_filter.all())

## UPDATE
first_tech=Tech.query.get(1)
first_tech.name='Riju'
db.session.add(first_tech)
db.session.commit()


print(Tech.query.all())