'''
st = "A:B:C:D"
s = st.split(":")

result = '#'.join(s)
print(result)
'''

print('#'.join("A:B:C:D".split(':')))