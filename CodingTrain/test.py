x = input().split('')
if 'img' in x[0]:
    print('image')
elif 'doc' in x[0]:
    print('document')
elif 'presen' in x[0]:
    print('presentation')
else:
    print('other')
