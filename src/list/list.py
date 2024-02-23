# Quick Examples to check if element contains in list

# Example 1: Consider list of integers
marks = [90, 56, 78, 90, 45]
print("Actual List: ", marks)

# Example 2: Using if statement
if 78 in marks:
    print("Exist!")
else:
    print("Not exist!")

# Example 3: Using count()
if marks.count(78) > 0:
    print("Exist!")
else:
    print("Not exist!")


# Example 5: Using index() with try-except block
try:
    marks.index(78)
    print("Exist!")
except:
    print("Not exist!")

# Example 6: Using any()
print(any(i == 99 for i in marks))

# Example 7: Using any() with filter()
print(any(list(filter(lambda x: x == 30, marks))))

# Example 8: String List

listStr = ["uno", "dos", "tres"]
print("Actual List: ", listStr)
if "unos" in listStr:
    print("Exist!")
else:
    print("Not exist!")


programming_languages = [
    {
        "user": "10310",
        "time_start": "2024-01-13 14:12:09.304291",
        "module": "connect",
    },
    {
        "user": "10311",
        "time_start": "2024-01-13 14:12:11.208800",
        "module": "connect",
    },
    {
        "user": "10312",
        "time_start": "2024-01-13 14:12:12.796904",
        "module": "connect",
    },
]

try:
    print(
        programming_languages.index(
            {
                "user": "10312",
                "time_start": "2024-01-13 14:12:12.796904",
                "module": "connect",
            }
        )
    )
except ValueError:
    print("That item does not exist")

# output
# That item does not exist


list_dict = [
    {"user": "102030", "module": "general"},
    {"user": "102031", "module": "general"},
]

 
list_dict_json = [
    {
        "user": "10310",
        "time_start": "2024-01-19 18:36:18.363489",
        "history": [
            {"module": "init session", "time_start": "2024-01-19 18:36:18.363489"}
        ],
    },
    {
        "user": "10312",
        "time_start": "2024-01-19 18:36:29.773667",
        "history": [
            {"module": "init session", "time_start": "2024-01-19 18:36:29.773667"}
        ],
    },
    {
        "user": "10311",
        "time_start": "2024-01-19 18:37:49.865982",
        "history": [
            {"module": "init session", "time_start": "2024-01-19 18:37:49.865982"}
        ],
    },
]

def find_user_discard(find, find_by, list_dict):
    return_element = [
        element for element in list_dict if element[f"{find_by}"] != find]
    return return_element

print(list_dict_json, "\n")
print(find_user_discard("10310", "user", list_dict_json))

def delete_user_connect(self, list_dict: list, find_by, find):
    for item in list_dict:
        if item[find_by] == find:
            list_dict.remove(item)

def update_dinamyc(find: str, find_by: str, list_dict: list, value_update, attribute: str):
 
    # Lista comprimida
    return_new_list = [element for element in list_dict if element.get(find_by) == find]

    if return_new_list:
        for element in return_new_list:
            # Actualiza dinámicamente el atributo especificado
            element[attribute] = value_update

    # Devuelve la lista actualizada o la original si no hubo cambios
    return return_new_list or list_dict


def update_user_module(find: str, find_by: str, list_dict: list, value_update, attribute: str):

    updated_list = []

    for element in list_dict:
        if element.get(find_by) == find:
            # Crea un nuevo diccionario actualizado
            updated_element = element.copy()            
            updated_element[attribute] = value_update
            updated_list.append(updated_element)
        else:
            updated_list.append(element)
            
    
    return updated_list

 
 

print("------------")
print(list_dict)
 
data = update_user_module(
    find="102030",
    find_by="user",
    list_dict=list_dict,
    attribute="module",
    value_update="invoice",    
)

print("------------")
print(data)

retorna = update_dinamyc(
    find="102031",
    find_by="user",
    list_dict=list_dict,
    attribute="module",
    value_update="invoice",    
)
print("------------")
print(retorna)


print("------------")
print(list_dict)