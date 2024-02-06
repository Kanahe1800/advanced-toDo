import os


def register(name, password, reenter):
    """
    This function allows user to create new account and register
    :return: nothing
    """
    if password == reenter:
        if not os.path.exists(name + ".txt"):
            open(name + ".txt", 'w').close()
            file_register = open("registered.txt", "a+")
            file_register.write(name + "," + password + "\n")
            file_register.close()
            print("registered")
            return True
        else:
            print("user name is already used")
            return False

    else:
        print("password does not match")
        return False


def login(registered_name, registered_password):
    """
    This function allows user to log into user's account
    :return: registered_name that is the username of the user
    """
    registered_list = []
    found = False
    file_registered = open("registered.txt", "r")
    # creating 2D list that contains name and password as a list
    for line in file_registered:
        content = line.strip()
        content_list = content.split(",")
        registered_list.append(content_list)
    # checking whether registered_name and registered_password is matched
    for elem in registered_list:
        if registered_name == elem[0] and registered_password == elem[1]:
            file_registered.close()
            found = True
            return found
    if not found:
        return False


def create_2d_list(file_name):
    """
    This function creates 2d array from the file that uses later
    :param: file_name - file name that will be open and read then create 2d array out
                of the data inside
    :return arr - 2d array that has 3 columns, and the number of rows is corresponding with the number of lines in the
    txt file
    """
    file = open(file_name + ".txt", "r")
    rows = 0
    element_list = []
    for line in file:
        if line != "\n":
            rows += 1
    arr = [["0" for i in range(3)] for j in range(rows)]
    file.seek(0)
    print(arr)
    for line in file:
        content = line.strip()
        content_list = content.split(",")
        element_list.append(content_list)
    print(element_list)
    for i in range(len(element_list)):
        for j in range(len(element_list[i])):
            arr[i][j] = element_list[i][j]
    print(arr)
    return arr


def write_on_file(file_name, element_list):
    """
    this function is used to store element of the list to the file
    :param: file_name - file name that will be open and write on each file includes all
                the elements of the element_list
    :param: element_list - 2d list that has created inside each function stated below
    :return nothing
    """
    clear_file = open(file_name + ".txt", "w+")
    for i in range(len(element_list)):
        if i != 0:
            clear_file.write("\n")
        for j in range(len(element_list[i])):
            if j == len(element_list[i]) - 1:
                clear_file.write(element_list[i][j])
            else:
                clear_file.write(element_list[i][j] + ",")
    clear_file.close()


def add_to_do(file_name, adding_element):
    """
    This function adds to do to the element_list created by function created_2d_list
    :param: file_name - username that is used in log in, and passes to the function write_on_file
    :return nothing it is there to finish the
    """
    element_list = create_2d_list(file_name)
    # print(element_list)
    adding_list = ["0" for i in range(3)]
    element_list.append(adding_list)
    for inner_list in element_list:
        if inner_list[0] == adding_element:
            print("no")
            return False
        else:
            position = len(element_list) - 1
            element_list[position][0] = adding_element
            write_on_file(file_name, element_list)
            return True
    # print(element_list)
    # write_on_file(file_name, element_list)


def delete_to_do(file_name, delete_element):
    """
    This function delete the to-do from the element_list that is created using create_2d_list as well as txt file
    :param file_name: the txt file that delete element is located
    :param delete_element: The element that should be chosen by users to delete
    :return:
    """
    element_list = create_2d_list(file_name)
    for elem in element_list:
        if elem[0] == delete_element:
            element_list.remove(elem)
            break
    write_on_file(file_name, element_list)
    return


def selected_date(calendar, file_name, selected_todo):
    """
    This function adds due date to the to-do that is selected by users
    :param calendar: this is tkcalendar that will be added when combining with graphical user interface
    :param file_name: the to-do that users want to add due date is located
    :param selected_todo: the to-do that users want to add due date
    :return:
    """
    element_list = create_2d_list(file_name)
    date = calendar.get_date()
    for i in range(len(element_list)):
        print(element_list)
        if element_list[i][0] == selected_todo:
            element_list[i][1] = date
            write_on_file(file_name, element_list)
            print(date)
            return
    print("alert")


def select_priority(file_name, selected_todo, selected_priority):
    """
    This function adds to-do to priority chosen by users
    :param file_name: the file name that to-do that users want to add priority is located
    :param selected_todo: the to-do that users want to add priority to
    :param selected_priority: the priority chosen by users
    :return:
    """
    element_list = create_2d_list(file_name)
    for i in range(len(element_list)):
        if element_list[i][0] == selected_todo:
            element_list[i][2] = selected_priority
            write_on_file(file_name, element_list)
            return
    print("alert")


