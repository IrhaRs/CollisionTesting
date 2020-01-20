from TestEnvironment import Environment
from Objects import ShapeObj

game = Environment.Environment()

#create object
poly1 = ShapeObj.Poly()
poly1.make_relative_point(0, -80)
poly1.make_relative_point(-50,50)
poly1.make_relative_point(50,50)
poly1.rotate(30)
poly1.debug = True


game.lst_objects.append(poly1)

game.run()