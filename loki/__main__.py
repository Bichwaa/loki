import fire
from loki import *

def mainFunc():
  fire.Fire({
      'enc': encrypt,
      'dec': decrypt,
      'decp' : decp
  })

  
if __name__ == '__main__':
  mainFunc()