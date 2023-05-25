
def validate_cradit_card(card_num:str):
    card_len=len(card_num)
    is_valid=False
    num_len={
        "4":13,
        "5":13,
        "6":15
    }
    if 13<=card_len<=16:
        if card_len==num_len[card_num[0]] or\
            (card_len==16 and card_num[:2]=="37"):
            even_nums=list(map(int,card_num[::-1][1::2])) #reverse, second's list
            odd_nums=list(map(int,card_num[::-1][0::2]))
            even_nums=[i*2 for i in even_nums]
            for i,n in enumerate(even_nums):
                if n>9:
                    while n%10:
                        even_nums.append((n%10))
                        n=int(n/10)
                    even_nums.pop(i)
            total=sum(even_nums)+sum(odd_nums)
            if total%10:
                is_valid=True
    return is_valid

card_num=input("Enter Valied card")
print(validate_cradit_card(card_num))