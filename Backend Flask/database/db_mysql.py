from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin:

    def insert (self):
        db.session.add(self)
        db.session.commit() 
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update (self):
        self.verified = True
        db.session.commit()

    @classmethod
    def execute_all(cls):
        return cls.query.all()


    @classmethod
    def execute_query(cls, **kwargs):
        """
        Ejecuta una consulta dada usando SQLAlchemy.

        Args:
            kwargs: Parámetros adicionales para la consulta.
                Ejemplo: username=username

        Returns:
            El resultado de la consulta.
        """
        try:
            #print("kwargs", kwargs,"cls", cls)
            row = db.one_or_404(db.select(cls).filter_by(**kwargs),)
            return row
        except Exception as e:
            print("An error occurred:", str(e))
            return False        
    @classmethod
    def execute_query_all(cls, **kwargs):
        try:
            query = db.session.query(cls)

            # Filter the query based on the provided keyword arguments
            for key, value in kwargs.items():
                query = query.filter(getattr(cls, key) == value)

            result = query.all()
            return result
        except Exception as e:
            print("An error occurred:", str(e))
            return False
