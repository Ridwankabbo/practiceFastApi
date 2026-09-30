from sqlmodel import Field, SQLModel, create_engine, Session, select
class Hero(SQLModel, table=True):
    
    id: int | None=Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    
sqlite_file_name = "database.db"
sqlite_url= f"sqlite:///{sqlite_file_name}"
    
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def create_hero():
    hero_1 = Hero(name="Dedpond", secret_name="Dive wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        
        session.commit()
        
def select_heros():
    with Session(engine) as session:
        # statement = select(Hero)
        results = session.exec(select(Hero)).all()
        print(results)
            
    
    
def main():
    create_db_and_tables()
    # create_hero()
    select_heros()
    
if __name__ == "__main__":
    main()

