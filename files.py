name = (input("whats your name"))
out_file = open ("name.txt" ,"w")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt" , "r")
first_num = int(in_file.readline())
secound_num = int(in_file.readline())
print(first_num + secound_num)
in_file.close()

