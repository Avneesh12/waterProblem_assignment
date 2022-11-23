"""Program of smart solution for water management to manage their water bills efficiently

Use ALLOT_WATER no.of BHK Corporate Water : Borewell Water     ------for allot the water
Use ADD_GUESTS no.of Guests                                   --for add guests

"""





class Myclass:                          #Class For Store The Bill And Water Use
    total_bill = []
    total_water_use = []
    guest_list = []

print("Enter Your Operation such as ALLOT_WATER 2 3:4 and then ADD_GUESTS ")
op1 = input("")


#Allot Water One Time in Whole Program
if op1.startswith('ALLOT_WATER'):
    try:
        slice_str = op1
        bhk = int(slice_str[11:13])
        ratio1 = int(slice_str[13:15])
        ratio2 = int(slice_str[16:17])
        if bhk == 2:
            fix_water_supply_ltr = 900
            ratio_value = 900 / (ratio1 + ratio2)
            Myclass.total_water_use.append(fix_water_supply_ltr)
            cor_water =  (ratio1 * ratio_value)
            borewell_water = fix_water_supply_ltr - cor_water
            total_rs = cor_water * 1 + borewell_water * 1.5
            Myclass.total_bill.append(total_rs)

        elif bhk == 3:
            fix_water_supply_ltr = 1500
            ratio_value = 1500/(ratio1+ratio2)
            Myclass.total_water_use.append(fix_water_supply_ltr)
            cor_water =  (ratio1 * ratio_value)
            borewell_water = fix_water_supply_ltr - cor_water
            total_rs = (cor_water * 1) + (borewell_water * 1.5)
            Myclass.total_bill.append(total_rs)

    except Exception as e:                  #If Any Exception Arrive Then It Will SHow(Print)
        print(e)


#Infinit Loop For Add Guests

while True:
    op = input("")
    if op.startswith('ADD_GUESTS'):
        str_slice = op
        guest = int(op[11:])
        Myclass.guest_list.append(guest)

    elif op == 'BILL':                      # One Time Bill Statement
        def add_guest(no_of_guest):
            tanker_water = no_of_guest * 10 * 30
            Myclass.total_water_use.append(tanker_water)
            tanker_water_rs = 0
            if tanker_water <= 500:
                tanker_water_rs = tanker_water * 2
            elif tanker_water >= 501 and tanker_water <= 1500:
                tanker_water = tanker_water - 500
                tanker_water_rs = tanker_water * 3 + 1000
            elif tanker_water >= 1501 and tanker_water <= 3000:
                tanker_water = tanker_water - 1500
                tanker_water_rs = tanker_water * 5 + 4000
            elif tanker_water > 3000:
                tanker_water = tanker_water - 3000
                tanker_water_rs = tanker_water * 8 + 5500
            return tanker_water_rs
        sum = 0
        for i in Myclass.guest_list:                        #Add the All Guests And Perform the Function
            sum = sum + i
        all_additional_supply_water = add_guest(sum)
        Myclass.total_bill.append(all_additional_supply_water)
        total_bill = 0
        for bill in Myclass.total_bill:
            total_bill = total_bill + bill
        print(int(abs(total_bill)))                                      #Bill

        water_used = 0
        for water in Myclass.total_water_use:
            water_used = water_used + water
        print(int(water_used))                                  #Water Used
        break
    else:
        print("Enter Valid Keyword")
        break






