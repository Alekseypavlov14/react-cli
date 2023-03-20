import sys, os
from write_file import write_file
from templates import *

# get cli arguments
args = sys.argv[1::]

# set variables from arguments
name = args[0]

path = 'src/components'
if len(args) > 1: 
  path = args[1]

# main process
if __name__ == '__main__':
  component_folder_path = os.path.join(os.getcwd(), path, name)
  
  try: 
    os.makedirs(component_folder_path)
    
    tsx_file_path = os.path.join(component_folder_path, f'{name}.tsx')
    write_file(tsx_file_path, get_tsx_file_content(name))
    
    css_file_path = os.path.join(component_folder_path, f"{name}.module.css")
    write_file(css_file_path, get_css_file_content(name))

    index_file_path = os.path.join(component_folder_path, "index.ts")
    write_file(index_file_path, get_index_file_content(name))
    
  except FileExistsError:
    print('This component is already exists')
  except PermissionError:
    print("You shouldn't use absolute path (which starts with '/')")