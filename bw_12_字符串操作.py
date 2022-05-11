str1 = "我的外号是'大西瓜'"
print(str1)

str2 = 'hello python'
# 索引
print(str2[2:9])

# 遍历字符串
for c in str2:
    print(c)

# 统计字符串长度
print(len(str2))

# 统计某个字符串出现的次数
print(str2.count("o"))

# 某个字符串出现的位置
print(str2.find("p"))

# 判断字符串中是否只包含空格或空白字符（\t、\n、\r）
print(str2.isspace())

str_space = "   \t\n\r"
print(str_space.isspace())

# 判断字符串中是否都是字母
print(str2.isalpha())

# 判断字符串中是否都是字母和数字
print(str2.isalnum())

# 判断字符串中每个单词的首字母是否大写（即标题化）
print(str2.istitle())

# 判断字符串中所有的字符都是小写
print(str2.islower())

# 判断字符串中所有的字符都是大写
print(str2.isupper())

