import os


def aaa(
    name,
    age: int,
    description,
):
    print(os.environ)
    print(
        name,
        age,
        description,
    )


aaa(
    "",
    111,
    "",
)


def aaa():
    ...
