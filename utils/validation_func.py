# Match Case , Recrusive()

def validation_int(prompt):
    try:
        x = int(input(prompt))
        if x < 0 or x == 0:
            raise ValueError
        else:
            return x
    except ValueError:
        print("Error: Please Enter a Valid Option")
        validation_int(prompt)

def validation_id(prompt,y):
    x = validation_int(prompt)
    r = False
    for i in y:
        if i == x:
            r = True
            break
    if r:
        print("Data Sudah Ada")
        validation_id(prompt,y)
    else:
        print("Data Tidak Ditemukan")
    return x


data = [1,2,3,4,5]
check_id = [i for i in data]
# x = validation_int("Random Number: ")

a = validation_id("ID Number: ",data)

print(a)