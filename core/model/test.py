from sqlmodel import Field, SQLModel, Relationship, create_engine, Session, select
from sqlalchemy import MetaData
from sqlalchemy.orm import selectinload
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

SQLModel.metadata= MetaData(naming_convention=naming_convention)

class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquaters: str
    
    heroes : list['Hero'] = Relationship(back_populates='team')

class Hero(SQLModel, table=True):
    
    id: int | None=Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    team_id: int | None = Field(default=None, foreign_key='team.id')
    
    team : Team | None = Relationship(back_populates='heroes') 
    

    
sqlite_file_name = "database.db"
sqlite_url= f"sqlite:///{sqlite_file_name}"
    
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def create_hero(item:Hero):
    # hero_1 = Hero(name="Dedpond", secret_name="Dive wilson")
    # hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    
    with Session(engine) as session:
        session.add(item)
        # session.add(hero_2)
        
        session.commit()
        
def create_team(item:Team):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        
def get_teams():
    with Session(engine) as session:
        results = session.exec(select(Team)).all()
        return results
    
def get_team_by_id(id):
    with Session(engine)as session:
        try:
            result = session.exec(
                select(Team).where(Team.id == id)
                .options(selectinload(Team.heroes))
            ).first()
            
            print(result)
            return result
        except Exception as e:
            return f"An error occured {e}"
def select_heros():
    with Session(engine) as session:
        # statement = select(Hero)
        results = session.exec(select(Hero)).all()
        print(results)
        return results

def select_hero(id):
    with Session(engine) as session:
        result = session.exec(select(Hero).where(Hero.id==id)).first()
        return result
            
    
    
def main():
    create_db_and_tables()
    # create_hero()
    # select_heros()
    
if __name__ == "__main__":
    main()

