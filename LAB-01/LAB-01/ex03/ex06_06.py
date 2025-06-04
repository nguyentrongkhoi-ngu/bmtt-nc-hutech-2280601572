def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'ee'
result = xoa_phan_tu(my_dict, key_to_delete)

if result:
    print("Phần tử đã được xóa khỏi dictionary:", my_dict)
else:
    print(f"Không tìm thấy phần tử với khóa '{key_to_delete}'")
