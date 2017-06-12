from sqlalchemy.orm import sessionmaker


# from bookinghotel.models import create_W73Transfer_table
class WBaseActions():
    """docstring for WBaseActions"""
    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)
        # create_W73Transfer_table(self.engine)
