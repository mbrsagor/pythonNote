name = "md.bozlur rosid sagor"
print(name.title())
print(name.replace('sagor', 'mbr-sagor'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.islower())
print(name.isupper())

print('\n')

address = "uttara Sector#14, Road#07, house#30, 5A"
print(address)
print(address.swapcase())

phn_num = '01773474709'
print(phn_num.isdigit())
print(phn_num.isdecimal())
print('\n')

"""
Here endswith return `True` or `False`
Only after dot(.) string only using endswith.
If after dot  string keep then `True` otherwise return `False` 
"""
company = 'http://google.com.bd'
print(company.endswith('bd'))
print(company.endswith('google'))

"""
Here `find` function return index.
And `split` function string convert list. 
"""
text = "Hello there I am a google software developer."
print(text.find('google'))
print(text.split())
print(type(text.split()))

print('\n')

"""
Here `strip` use for remove `=` equal 
And also `strip` function remove world, text, speach and whatever you want... 
"""
first_name = "=================mbr=================="
print(first_name)
print(first_name.strip('='))
print(first_name.lstrip('='))
print(first_name.rstrip('='))
