def tuples():
    print('                          ')
    print("""Tuples behave like lists and only differ in that tuples are immutable
              """)
    list1 = ['John', 'Mary', 'Andrew', 'Shyrine', 'Samuel']
    tuple1 = tuple(list1)
    print(tuple1)
    print(tuple1.index('John'))
    tuple1.count('Mary')
    print('                      ')
    print('Unpacking tuples')
    anotherTuple = 'Andrew', '12', '143 cm'
    name, age, height =  'Andrew', '12', '143 cm'
    print(name,age,height)
    numLists = [12, 43, 65, 33, 90]
    tuple_num =tuple(numLists)
    i1, *i2, ilast = tuple_num
    print(i1,)
    print(i2)
    print(ilast)


tuples()