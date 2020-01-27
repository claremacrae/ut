import subprocess


def run(command):
    print(command)
    subprocess.run(" ".join(command), shell=True, check=True)