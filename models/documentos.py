from config.database import base
from sqlalchemy import Column, String

class Documentos(base):
    
    __tablename__ = "papers"
    
    id = Column(String, primary_key = True)
    submitter = Column(String)
    authors = Column(String)
    title = Column(String)
    comments = Column(String)
    journal_ref = Column(String)
    doi = Column(String)
    report_no = Column(String)
    categories = Column(String)
    license = Column(String)
    abstract = Column(String)
    versions = Column(String)
    version = Column(String)
    created = Column(String)
    update_date = Column(String)
    authors_parsed = Column(String)