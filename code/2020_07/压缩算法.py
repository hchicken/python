#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 21:38
# @Author  : Greens


"""
小Q想要给他的朋友发送一个神秘字符串，但是他发现字符串的过于长了，
于是小Q发明了一种压缩算法对字符串中重复的部分进行了压缩，
对于字符串中连续的m个相同字符串S将会压缩为[m|S](m为一个整数且1<=m<=100)，
例如字符串ABCABCABC将会被压缩为[3|ABC]，现在小Q的同学收到了小Q发送过来的字符串，你能帮助他进行解压缩么？


输入第一行包含一个字符串s，代表压缩后的字符串。
S的长度<=1000;
S仅包含大写字母、[、]、|;
解压后的字符串长度不超过100000;
压缩递归层数不超过10层;


输出描述:
输出一个字符串，代表解压后的字符串。

输入例子1:
HG[3|B[2|CA]]F

输出例子1:
HGBCACABCACABCACAF

例子说明1:
HG[3|B[2|CA]]F−>HG[3|BCACA]F−> HGBCACABCACABCACAF
"""


class Solution:
    def getString(self, my_strings):
        # 模拟一个栈
        my_list1 = []
        # 开始遍历
        for my_string in my_strings:
            my_list1.append(my_string)
            if my_string == "]":
                a = my_list1.pop()
                my_str1 = a
                while a != "[":
                    a = my_list1.pop()
                    my_str1 = a + my_str1
                my_list2 = my_str1[1:-1].split("|")
                my_list1.append(int(my_list2[0]) * my_list2[1])
        return "".join(my_list1)


if __name__ == '__main__':
    my_class = Solution()
    my_str = "HG[3|B[2|CA]]F"
    my = my_class.getString(my_str)
    print(my)
