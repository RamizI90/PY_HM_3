#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

def main():
    number_list = [9, 3, 8, 6, 4, 7]
    product = 1
    multiplier1 = number_list[0]
    multiplier2 = number_list[-1]
    
    product_list = []
    for i in range((len(number_list)+1)//2):
        product_list.append(number_list[i]*number_list[len(number_list)-1 - i])


       
    print('Произведение из пар  = ', product_list)

main()