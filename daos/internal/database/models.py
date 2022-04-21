from datetime import datetime


from sqlalchemy import Column, DateTime, BigInteger, String, Boolean

from daos.abstracts.database.model import BaseDBModel
from daos.abstracts.database.config import Base


class DocumentIndexModel(BaseDBModel, Base):
    retrieved_from_web_at = Column(DateTime(True), default=datetime.utcnow)

    url = Column(String)
    document_id = Column(BigInteger)

    raw_html_version_document_path = Column(String)
    raw_html_pdf_version_document_path = Column(String)
    html_only_version_document_path = Column(String)
    html_only_pdf_version_document_path = Column(String)

    is_raw_html_version_stored = Column(Boolean, default=False)
    is_raw_html_pdf_version_stored = Column(Boolean, default=False)
    is_html_only_version_stored = Column(Boolean, default=False)
    is_html_only_pdf_version_stored = Column(Boolean, default=False)

    is_type_google_search_results = Column(Boolean, default=False)

    google_search_results_query = Column(String)
