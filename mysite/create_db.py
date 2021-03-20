from app.models import Home
import random as _

for models_in_range in range(10000):
    Home.objects.create(city = _.randint(1, 5), adress = _.randint(1, 8), date = _.randint(1, 12), temp = _.randint(400, 900), aqua_cold = float(_.randint(1, 5) + _.randint(1, 10) // 10), aqua_hot = float(_.randint(1, 5) + _.randint(1, 10) // 10), el = _.randint(70, 500))
    