from retrival.hybird_search import HybridSearch
from retrival.re_ranking import Re_Ranking
from generation.core import model

model = model()
hybird_search = HybridSearch()


hybird_search.query.invoke("hello")
