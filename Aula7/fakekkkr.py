from faker import Faker
import pandas as pd
fake = Faker("pt_BR")

nome = ("Nome:", fake.name())
email = ("Email:", fake.email())
cidade = ("Cidade:", fake.city())

usuario = [nome, email, cidade]

printar = pd.DataFrame(usuario)
print(printar)
