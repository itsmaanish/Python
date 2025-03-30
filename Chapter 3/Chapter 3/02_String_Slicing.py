# String Slicing  --> {#len - 1}
                                  #  M a n i s h
name = "Manish" #index of Manish --> 0 1 2 3 4 5
res = name[1:5]   
print(res)

# Slice with Skip value
str = "abcdefghijklmnopqrstuvwxyz"
res = str[1:9:3]  #[1:9] --> bcdefghi  --> [1:3]--> b jump 3 times --> beh
print(res)

# Advance Slicing Technique
sen = "Hello Nice to meet you!!"
res = sen[:5]  #[0:5] --> Hello
res1 = sen[:8]  #[0:8] --> Hello Ni
res2 = sen[4:] #[4:(len-1)] --> o Nive to meet you!!
print(res)
print(res1)
print(res2)



