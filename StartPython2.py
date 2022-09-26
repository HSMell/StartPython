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
for k, v in person.items():
    print(x, v);

fruit = 'apple';
for x in fruit:
    print(x);


# While
max = 25;   #Maximum allowable weight
weight = 0; #Current Weight
item = 3;   #The weight of each package

while weight + item <= max:
    weight += item;
    print('Add your luggage');
print('My weight is {}'.format(weight));
print('My weight is {weight}'.format(weight = weight));

# Break;
drama = ['season1','season2','season3','season4','season5'];
for x in drama:
    print('I watched {}'.format(x));
    if x == 'season3':
        print('{} is not so funny'.format(x));
        break;
print('Done with Breaking');
print('------------------');

# Continue
drama = ['season1','season2','season3','season4','season5'];
for x in drama:
    if x == 'season3':
        print('{} is not so funny'.format(x));
        continue
    print('{} watching'.format(x));
print('Done with continue');
print('------------------');