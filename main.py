# 1-m
counter = 0

def oshir():
    global counter
    counter += 1

oshir()
print(counter)


# 2-m
summa = int(input("Son kirit: "))

def qosh():
    global summa
    summa += summa

qosh()
print(summa)


# 3-m
text = " "

def qosh():
    global text
    text += text

qosh()
print(text)


# 4-m
max_val = 0

def tekshir(son):
    global max_val
    max_val = max(max_val, son)

tekshir(5)
tekshir(12)
tekshir(7)
print(max_val)


# 5-m
counter = 10

def kamaytir():
    global counter
    counter -= 2

kamaytir()
print(counter)


# 6-m
numbers = []

def qosh_son(son):
    global numbers
    numbers.append(son)

qosh_son(3)
qosh_son(8)
print(numbers)


# 7-m
is_active = False

def faollashtir():
    global is_active
    is_active = True

faollashtir()
print(is_active)


# 8-m
balance = 100

def ayir(summa):
    global balance
    balance -= summa

ayir(30)
print(balance)


# 9-m
balance = 0

def toldir(summa):
    global balance
    balance += summa

toldir(50)
toldir(25)
print(balance)


# 10-m
users = []

def qosh_user(i):
    global users
    users.append(i)

qosh_user("Ali")
qosh_user("Vali")
print(users)


# 11-m
temperature = 20

def set_temp(i):
    global temperature
    temperature = i

set_temp(30)
print(temperature)


# 12-m
product_count = 0

def add_pro():
    global product_count
    product_count += 1

add_pro()
add_pro()
print(product_count)


# 13-m
history = []

def add_history(i):
    global history
    history.append(i)

add_history("login")
add_history("search")
print(history)


# 14-m
flag = False

def teskari():
    global flag
    flag = not flag

teskari()
print(flag)


# 15-m
score = 0

def scores(ball):
    global score
    score += ball

scores(10)
scores(5)
print(score)


# 16-m
score = 100

def kamaytirish(i):
    global score
    score -= i

kamaytirish(10)
print(score)


# 17-m
items = [1, 2, 3, 4]

def ochir(x):
    global items
    items.remove(x)

ochir(3)
print(items)


# 18-m
visits = 0

def sayt():
    global visits
    visits += 1

sayt()
sayt()
sayt()
print(visits)


# 19-m
password = "1234"

def ozgartir():
    global password
    password = "5678"

ozgartir()
print(password)


# 20-m
log = []

def logs(i):
    global log
    log.append(i)

logs("Start")
logs("Stop")
print(log)


# 21-m
likes = 0

def like():
    global likes
    likes += 1
  
like()
like()
print(likes)


# 22-m
dislikes = 0

def dislike ():
    global dislikes
    dislikes += 1
  
dislike()
print(dislikes)


# 23-m
cart = []

def savat(item):
    global cart
    cart.append(item)
  
savat("Olma")
savat("Banan")
print(cart)


# 24-m
cart = []

def carts(item):
    global cart
    if item in cart:
        cart.remove(item)
      
carts("Olma")
print(cart)


# 25-m
users = 0

def login():
    global users
    users += 1
def user_logout():
    global online_users
    online_users -= 1
  
login()
login()
user_logout()
print(users)


# 26-m
level = 1

def level_up():
    global level
    level += 1
  
level_up()
level_up()
print(level)


# 27-m
energy = 100

def use_energy(val):
    global energy
    energy -= val
  
use_energy(10)
use_energy(20)
print(energy)


# 28-m
messages = []

def add_message(msg):
    global messages
    messages.append(msg)
  
add_message("Salom")
add_message("Xayr")
print(messages)


# 29-m
errors = 0

def add_error():
    global errors
    errors += 1
  
add_error()
add_error()
print(errors)


# 30-m
discount = 0

def set_discount(val):
    global discount
    discount = val
  
set_discount(15)
print(discount)


