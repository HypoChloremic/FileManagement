from os import walk
import os, shutil

class Expander:
  def __init__(self):
    self.ev = [".h", ".cpp"]

  def bol(self, n):
    for i in self.ev:
      if i in n:
        return True
    return False

  def expander(self, top, delimiter="/"): #, bol_=lambda i: True if (".h" or ".cpp" in i)):
    walk_gen = walk(top)
    paths    = []

    for i in walk_gen:
      for n in i[1:]:
        for k in n:

          if self.bol(k):
            paths.append((i[0],k))

    base     = os.getcwd() + "/official/"
    abspaths = []

    for i in paths:
      fr = "/".join(i)
      to = f"{base}{os.path.relpath(fr)}"
      abspaths.append((fr, to))

    return abspaths

  def copy(self, src: str, dest: str):
    dest_dir = os.path.dirname(dest)
    try:
      os.makedirs(dest_dir)
    except os.error as e:
      print(f"os.error: {e}")
    shutil.copy(src, dest)

if __name__ == '__main__':
  path = os.getcwd()
  print(f"Current wd: {path}")
  run = Expander()
  abspath = run.expander(path)
  for i in abspath:
    run.copy(i[0], i[1])