##controller de la calculatrice

import shunting_yard as sy
from shunting_yard.rpn import WrongExpressionError
from app.classs.interfaces.Icontroller import Icontroller
from app.classs.entities.Calcul import Calcul

class calculCTRL(Icontroller):
    def post(self, item):
        try:
            calcul = self.format(item)
            result = sy.compute_rpn(calcul)
            Calcul.create(calcul=calcul, result=result)
            return result
        except WrongExpressionError:
            return "erreur "
        except Exception:
            return "Une erreur inattendue est survenue"
    def get(self):
        pass
    def format(self, item):
        item = item.replace(":", "/")
        item = item.replace(",", " ")
        return item