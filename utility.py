from algo1 import substr,strcmp,String

def printHelp(name):
  print(f"""USAGE:
  {name} --create <path_name>: creates library structure using directory <path_name>.
  Files must be *.txt
  {name} --search <word>: searches <word> in library
  {name} --help: shows this message""")

def cleansubstr(text,start,end,max):
  if start >= max:
    return String("")
  unproperEnd = String(")]}>\"!?.,:;")
  unproperStart = String("([{<\"")
  for i in range(len(unproperEnd)):
    if strcmp(text[end-1],unproperEnd[i]):
      end -= 1
      return cleansubstr(text,start,end,max)
  for i in range(len(unproperStart)):
    if strcmp(text[start],unproperStart[i]):
      start += 1
      return cleansubstr(text,start,end,max)
  return substr(text,start,end)
