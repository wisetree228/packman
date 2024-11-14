from objects.base import BaseObject


class Field(BaseObject):
    def __init__(self, path_to_file = '/home/prom/PycharmProjects/pacman-py-masters/scenes/field.txt'):
        self.l=[] # создаём двумерный массив который соответствует файлу field.txt
        f = open(path_to_file)
        f = [str(i) for i in f.readlines()]
        for i in range(len(f)):
            self.l.append([])
            for j in f[i]:
                if j!='\n':
                    self.l[i].append(j)




