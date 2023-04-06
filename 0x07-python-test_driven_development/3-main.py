#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Ruth", "Arimuk")
say_my_name("Florence", "Chemsto")
say_my_name("Daniel")
try:
    say_my_name(10, "Blue")
except Exception as e:
    print(e)
