#numbers = [1,2,3,4,5,6,7,8,9,10]

#carres = [i*i for i in numbers]

#print(carres)


#numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#evens_numbers = [i%2==0 for i in numbers]

#evens_numbers = [i for i in numbers if i%2==0]

#print(evens_numbers)


sentence = input("Enter a sentence: ")
sentence_cut = sentence.split()
liste = [i.upper() for i in sentence_cut if len(i)>3]
print(liste)