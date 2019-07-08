from sqlalchemy import Column, FLOAT, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class DataSet(DeclarativeBase):
    __tablename__ = 'dataset'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    channel = Column(String)
    country = Column(String)
    os = Column(String)
    impressions = Column(Integer)
    clicks = Column(Integer)
    installs = Column(Integer)
    spend = Column(Integer)
    revenue = Column(FLOAT)

    def to_json(self):
        return {
            "date": self.date,
            "channel": self.channel,
            "country": self.country,
            "os": self.os,
            "impressions": self.impressions,
            "clicks": self.clicks,
            "installs": self.installs,
            "spend": self.spend,
            "revenue": self.revenue
        }
