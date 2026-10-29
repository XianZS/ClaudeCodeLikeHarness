import os
import sys

sys.path.append(os.getcwd())
from s01_agent_loop import code


def test_run_bash():
    result = code.run_bash("ls -l")
    print(result)


def test_agent_while():
    query = input("请输入问题:\n")
    history = [
        {"role": "user", "content": query},
    ]
    code.agent_loop(history)


if __name__ == "__main__":
    test_agent_while()
