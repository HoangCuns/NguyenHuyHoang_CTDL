# File: mymodule.py
print("The name of this module is", __name__)  # In ra "The name of this module is __main__"
# File: theimporter.py
import mymodule
print("Notice that it will print something different when imported?")  # In ra Here is how we use the name attribute to check how the program is
being run.
# File: mymodule.py
def somefunction():
    print("Real important stuff here..")
if __name__ == '__main__':
    somefunction()
