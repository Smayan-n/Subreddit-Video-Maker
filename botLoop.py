import subprocess

def main():

    for i in range(10):
        print(f"----------------------------------------VIDEO {i + 1}----------------------------------------")

        cmd = ['python', 'main.py']
        subprocess.Popen(cmd).wait()


if __name__ == '__main__':
    main()