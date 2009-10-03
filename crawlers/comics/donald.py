from crawlers.base import BaseComicCrawler
from datetime import date

class Donald(BaseComicCrawler):
	def __init__(self):
		super(Donald, self).__init__('Donald', 'donald.no', 30, 'Norske')
		self.url = "http://www.donald.no/upload/Forside/dagensstripexml/images/%s/big/stripestor_%s.gif" % (self.date.year, self.date.strftime("%d_%m_%Y"))