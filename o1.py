import math

import matplotlib.pyplot as plt
import numpy as np

from ppp import find_all_sums
print(math.floor(4.5))
print(math.ceil(4.5))
list1 = [1, 2]
list1.pop()
print(list1)
def generate_arrays(max_length, max_value):
  """Generates arrays recursively.

  Args:
    max_length: Maximum length of an array.
    max_value: Maximum value for elements in an array.

  Returns:
    A list of arrays.
  """

  if max_length == 0:
    return [[]]

  result = []
  for i in range(1,max_value + 1):
    for subarray in generate_arrays(max_length - 1, max_value):
      result.append([i] + subarray)

  return result

# Example usage:
max_length = 5
max_value = 3
arrays = generate_arrays(max_length, max_value)
print(arrays)



list1 = [1, 2]
list2 = [3]
# list1.remove()
print(list1)
result = [x + y for x, y in zip(list1, list2)]
print(result)  # Output: [4, 6]
print([1,2].append([3,4]))
#build binom vectors
matrix_b=[]
for i in range(10):
    vector_i=[]
    for j in range(10):
        vector_i.append(math.comb(i,j))
    matrix_b.append(vector_i)
print(matrix_b)
m=np.array(matrix_b)
m=m
print(m)

#build jumping
qlick_edges=[0]
for i in range(1,10):
    qlick_edges.append(qlick_edges[i-1]+i)
print(qlick_edges)
jump={}
jump1=[]
for i in range(len(qlick_edges)):
    for j in range(i):
        ju=qlick_edges[i]-qlick_edges[j]
        jump1.append(ju)
        # print(jump[ju])
        try:
            jump[ju]+=[(j,i)]
        except:
            jump[ju]=[(j,i)]
# print(jump1)
print(set(jump1))
# print(len(jump1))
print(jump)
nums = []
for n in jump1:
    for i in range(45//n):
        nums.append(n)

target_sum = 7
all_possible_sums = find_all_sums(nums, target_sum)
# print(all_possible_sums)


#todo למצוא את כל האפשרויות להרכיב מספר מחיבור של המספרים בסט לאחר מכן כל מספר בודד לנסות בכל אחת מהאפשרויות במילון
#todo לדוגמה 3 ניתן להרכיב מ2+1 ומ 1+1+1 3כל אחד מהמספרים לנסות את כל האפשריות שבימלון במקרה פה אפשרות אחת עבור אחת אפשרות אחת עבור 2 ו2 אפשריות עבור 3
#לאחר מכן ניצור את כל הפולינומים האפשרים לעצים עם n קודקודים
#בנייה
#10->45->45^2
#o(n^4)
#לאחר בנייה חד פעמית ניתן להריץ את כלל הבדיקות
#
#עבור n
# ניצור את כל החילוקים האפשריים של הדו צדדי כאשר הצד הגדול בין חצי ל n-1
# עבור כל עץ נמצא את מספר הצלעות שלא קיימות בגרף ונייצר אותם על ידי הרכבה של קליקות על פי הטבלה בגודל n^4
#נקבל את כל הפולינום העצמיים שיכולים להיות בעצים
#נבדוק יונימודליות עבור הפולינומים
#
#
# for i in range(5,10):
#     a=i
#     b=10-i
#
#
#
# print(math.comb(5, 2))
# for i in range(1,10):
#     print( 'n=',i)
#     for j in range(1,i):
#         print(math.comb(i,j),end=" ")
#     print()
# # for i in range(20,40):
# #     a=i
# #     b=40-a
# #     x=range(a)
# #     y=[(math.comb(a,j)+math.comb(b,j))for j in x]
# #     plt.plot(x, y)  # Plot the line using x and y data
# #
# #     # Add labels and title for clarity
# #     plt.xlabel("X-axis")
# #     plt.ylabel("Y-axis")
# #     plt.title('a= \{a}')
# #
# #     # Display the plot
# #     plt.show()
#
# # x = range(0, 100)  # Generate x-axis values (0 to 99)
# # y = [math.sin(i * math.pi / 50) for i in x]  # Calculate sine values for each x
#
#
#
#
#
#
#
#
#
#
#
#
#
