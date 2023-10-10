# Logging
import logging

#debug    - Só estou informando informações para desenvolvedores
#info     - Só quero informar algo que está acontecendo no programa, mas que não é um erro
#warning  - Quero alertar sobre algo que está acontecendo, possivelmente fora do esperado, porém ainda não é erro, mas pode gerar um futuramente
#error    - Um erro ocorreu na aplicação
#critical - Um erro com consequências graves acaba de ocorrer na aplicação
 
logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='a', format='%(levelname)s - %(message)s') # Setar o nível
logging.debug('Logging no nivel debug')
logging.info('Logging no nivel info')
logging.warning('Logging no nivel warning')
logging.error('Logging no nivel error')
logging.critical('Logging no nivel critical')
