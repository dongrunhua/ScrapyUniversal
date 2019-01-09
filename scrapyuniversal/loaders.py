from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()

class ChinaLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(), lambda s: s.strip(), lambda s: s.replace('\u3000', ''), lambda s: s.replace('\n', ''),
                          lambda s: s.replace('\xa0', ''), lambda s: s.replace('\r', ''),lambda s:s.replace('\t',''))

class WallStreetLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())
    datetime_out = Compose(Join(), lambda s: s.strip())
    digest_out = Compose(Join(), lambda s: s.strip())
    title_out = Compose(Join(),lambda s:s.strip())


class FinanceLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(),lambda s:s.replace("\u3000",''),lambda s:s.replace("\n",''),
                          lambda s: s.replace('\r',''),lambda s:s.replace('\\xao',''))
    source_out = Compose(Join(), lambda s: s.strip())
    # datetime_out = Compose(Join(), lambda s: s.strip())
    title_out = Compose(Join(), lambda s: s.strip())


class ChinaCourtLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''),lambda s:s.replace('\r',''))
    source_out = Compose(Join(), lambda s: s.strip())


class ChinaLawCourtLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''),lambda s:s.replace('\r',''))
    message_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))
    title_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))


class ChinaMessageLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''),lambda s:s.replace('\r',''),lambda s:s.replace('\t',''))
    # message_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))
    title_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))

class HuaLvLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''),lambda s:s.replace('\r',''),lambda s:s.replace('\t',''))
    # message_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))
    title_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))

class QiDianLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''),lambda s:s.replace('\r',''),lambda s:s.replace('\t',''))
    # message_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))
    chapter_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))

class XueQiuLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''),lambda s:s.replace('\r',''))
    # message_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))
    title_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))

class SinaFinanceLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(), lambda s: s.replace('\u3000', ''), lambda s: s.replace('\n', ''),
                          lambda s: s.replace('\xa0', ''), lambda s: s.replace('\r', ''),lambda s:s.replace('\t',''))
    # message_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))
    title_out = Compose(Join(), lambda s: s.strip(), lambda s: s.replace('\u3000', ''), lambda s: s.replace('\n', ''),
                        lambda s: s.replace('\xa0', ''))

class DefaultLoader(NewsLoader):
    content_out = Compose(Join(), lambda s: s.strip(), lambda s: s.replace('\u3000', ''), lambda s: s.replace('\n', ''),
                          lambda s: s.replace('\xa0', ''), lambda s: s.replace('\r', ''),lambda s:s.replace('\t',''))
    # message_out = Compose(Join(), lambda s: s.strip(),lambda s: s.replace('\u3000',''),lambda s:s.replace('\n',''),lambda s:s.replace('\xa0',''))
    title_out = Compose(Join(), lambda s: s.strip(), lambda s: s.replace('\u3000', ''), lambda s: s.replace('\n', ''),
                        lambda s: s.replace('\xa0', ''))
