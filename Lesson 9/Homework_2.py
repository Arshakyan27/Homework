# # Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
# # columns

# for a in range(1,6):
#     for b in range(1,6):
#         print("*", end="")
#     print("\n")
        
for a in range(5):
    m = ""
    for b in range(5):
        m += "*"
    print(m)