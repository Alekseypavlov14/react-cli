def write_file(path: str, content: str):
  file = open(path, 'a')
  file.write(content)
  file.close()