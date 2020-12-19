# https://edabit.com/challenge/sKNcrdJT4MpPfESrM
#
# Your computer might have been infected by a virus! Create a function that finds the viruses in files and removes
# them from your computer. Examples
#
# remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg") ➞ "PC Files: spotifysetup.exe, dog.jpg"
#
# remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") ➞ "PC Files:
# antivirus.exe, cat.pdf"
#
# remove_virus("PC Files: notvirus.exe, funnycat.gif") ➞ "PC Files: notvirus.exe, funnycat.gif")
#
# Notes
#
#     Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
#     Return "PC Files: Empty" if there are no files left on the computer.


def remove_virus(files):
    a, b, c = 0, 0, 0
    while a != len(files):
        if files[a] == " " and b == 0:
            a += 1
            b = a
        elif files[a] == " " and b != 0:
            c += files.index(files[a], a)
            a += 1
        elif " " not in files[a:]:
            if len(files) > 10:
                return files
            else:
                return "PC Files: Empty"
        else:
            a += 1

        if c != 0:
            if files[b:c].find("antivirus") != -1:
                a = c
                b, c = 0, 0
            elif files[b:c].find("notvirus") != -1:
                a = c
                b, c = 0, 0
            elif files[b:c].find("virus") != -1:
                a = b
                files = files[0:b] + files[c + 1:]
            elif files[b:c].find("malware") != -1:
                a = b
                files = files[0:b] + files[c + 1:]
            else:
                a = c
                b, c = 0, 0

    return files


print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(remove_virus("PC Files: notvirus.exe, funnycat.gif"))
print()