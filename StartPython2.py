# If
today = 'tuseday';
tommorow = 'tommorw';

if today == 'tuseday2':
    print('tuseday2!');
elif today == 'tuseday':
    print('tuseday');
else:
    print(tommorow);

yellow_card = 0;
foul = True;
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('Leave!');
    else:
        print('be careful plz');
else:
    print('be careful');

# For
for x in range(10):
    print('push up');
    print(x);

for x in range(1,10):
    print('chin up');
    print(x);

for x in range(1,10,2):
    print('chin up');
    print(x);
print('Done!');

my_list = [1,2,3];
for x in my_list:
    print('This is list');
    print(x);

my_tuple = (1,2,3);
for x in my_tuple:
    print('This is tuple');
    print(x);

person={'name' : 'KHS', 'age' : '29', 'weight' : ''};
for x in person.values():
    print(x);