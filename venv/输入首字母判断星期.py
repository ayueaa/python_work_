while True:
    first_letter=input("请输入星期首字母,输入q退出：")
    if first_letter=="s":
        sec_letter=input("请输入第二个字母：")
        if sec_letter=="a":
            print("It's Saturday")
        elif sec_letter=="u":
            print("It's Sunday")
    elif first_letter=="t":
        sec_letter = input("请输入第二个字母：")
        if sec_letter=="u":
            print("It's Tuesday")
        elif sec_letter=="h":
            print("It's Thursday")
    elif first_letter=="m":
        print("It's Monday")
    elif first_letter=="w":
        print("It's Wednesday")
    elif first_letter=="f":
        print("It's Friday")
    elif first_letter=="q":
        break
    else:
        print("输入有误，请输入星期首字母")

