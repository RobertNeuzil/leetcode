"""
Use a recursion function to find out when the father will be twice as old as his son
"""
def father_son(fatherAge, sonAge):
    while sonAge < 1000:
    
        if fatherAge / 2 == sonAge:
            print (f"The father will be twice as old as the son when the son is {sonAge} and the father is {fatherAge}")
            return True
        else:
            return father_son(fatherAge + 1, sonAge + 1)
    
    print (f"those parameter can not be met")
    return False

father_son(62, 23)