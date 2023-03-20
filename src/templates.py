def get_tsx_file_content(name: str):
  file_lines = [
    "import { FC } from 'react'",
    "import styles from './<COMPONENT>.module.css'",
    "",
    "interface <COMPONENT>Props {}",
    "",
    "export const <COMPONENT>: FC<<COMPONENT>Props> = () => {",
    "  return (",
    "    <div className={styles.<COMPONENT>}>",
    "      ",
    "    </div>",
    "  )",
    "}"
  ]
  
  file_content = '\n'.join(file_lines).replace('<COMPONENT>', name)
  
  return file_content

def get_css_file_content(name):
  file_lines = [
    ".<COMPONENT> {",
    "  ",
    "}"
  ]
  
  file_content = '\n'.join(file_lines).replace('<COMPONENT>', name)
  
  return file_content

def get_index_file_content(name: str):
  file_lines = [
    "export { <COMPONENT> } from './<COMPONENT>'"
  ]

  file_content = '\n'.join(file_lines).replace('<COMPONENT>', name)

  return file_content