import scratchattach as scratch3

username = input("insert your scratch username: ")
password = input("to end the login insert your password: ")
project_id = input("insert the project id: ")
variable = input("insert the cloud variable's name: ")
value = int(input("insert the value to set(only integer): "))
session = scratch3.login(username, password)
conn = session.connect_cloud(project_id)
conn.set_var(variable, value)
print("variable changed")
