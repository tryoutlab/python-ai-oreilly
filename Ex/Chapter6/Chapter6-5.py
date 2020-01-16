#!/usr/bin/env python
# coding: utf-8

# In[2]:


from kanren import run, var, fact
import kanren.assoccomm as la

# 足し算(add)と掛け算（mul)
# addとmulはルールの名前なだけ
add = 'addition'
mul = 'multiplication'

# 足し算、掛け算は交換法則（commutative)、結合法則(associative)を持つ事をfactを使って宣言する
# 交換法則とは、入れ替えても結果が変わらない事。足し算も掛け算も入れ替えても答えは変わらない
# 結合法則とは、カッコの位置を変えても変わらない事。足し算だけの式、掛け算だけの式はカッコの位置が変わっても答えは変わらない
# 交換法則も結合法則も文字列をどう扱うかといったルールでも使える
fact(la.commutative, mul)
fact(la.commutative, add)
fact(la.associative, mul)
fact(la.associative, add)

a, b, c = var('a'), var('b'), var('c')

expression_orig = (add, (mul, 3, -2), (mul, (add, 1, (mul, 2, 3)), -1))

expression1 = (add, (mul, (add, 1, (mul, 2, a)), b), (mul, 3, c))
expression2 = (add, (mul, 3, c), (mul, b, (add, (mul, 2, a), 1)))
expression3 = (add, (add, (mul, (mul, 2, a), b), b), (mul, 3, c))


# この式を例に
# 
# $$
#   expression\_orig = 3 \times (-2) + (1 + 2 \times 3) \times (-1)
# $$
# 
# 変数で置き換えた式を照合する
# 
# $$
# \begin{align}
#   &expression1 = (1 + 2 \times a) \times b + 3 \times c\\ 
#   &expression2 = c \times 3 + b \times (2 \times a + 1)\\
#   &expression3 = (((2 \times a) \times b) + b) + 3 \times c
#  \end{align}
# $$
# 
# expression1〜3は数学的に同じ式

# In[3]:


print(run(0, (a, b, c), la.eq_assoccomm(expression1, expression_orig)))
print(run(0, (a, b, c), la.eq_assoccomm(expression2, expression_orig)))
print(run(0, (a, b, c), la.eq_assoccomm(expression3, expression_orig)))


# 1番目と2番目の式は一緒。３番目は構造的に異なる（らしい）
# 
# run(答えの個数, （欲しい答えの変数）, 
# 
# 分配法則を定義していないから？？

# `eq_assoccomm`が分からん。。。
# 
# 
# 
