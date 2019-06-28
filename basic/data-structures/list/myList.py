nums = [30, 40, 10, 56, 88, 67, 25]
print(nums[0])
print(nums[1:3])
print(nums[3:6])
print(nums[-1])
print(nums[-7])
print(nums.insert(0, 5))
print(nums.append(100))
print(nums.pop(0))
print(nums.remove(56))
print(nums.reverse())
print(nums.sort())

print('\n')
for num, n in enumerate(nums):
    print(num, n)

print('\n')
print(min(nums))
print(max(nums))
print(sum(nums))

print('\n')

names = ['mbr-sagor', 'russel-mahmud', 'saif-nirob']
names[0] = "Md.Bozlur Rosid Sagor"
print(names[0])

del names[2]
print(names)
names.extend(['masba-rumi'])
print(names)

print('\n')

for name, val in enumerate(names):
    print(name, val)