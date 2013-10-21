"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "1. Basics": [
        {
            "input": [
                [1, 2, 3],
                [3, 1, 2],
                [2, 3, 1]]
        },
        {
            "input": [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
        },
        {
            "input": [
                [1, 2, 2],
                [2, 1, 2],
                [2, 2, 1]]
        },
        {
            "input": [
                [1, 2, 4],
                [4, 1, 2],
                [2, 4, 1]]
        },
        {
            "input": [
                [1, 3, 2],
                [2, 1, 3],
                [3, 2, 1]]
        },

    ],
    "2. Extra": [
        {
            "input": [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
        }


    ]
}

for cat in TESTS.keys():
    for t in TESTS[cat]:
        t["answer"] = t["input"]